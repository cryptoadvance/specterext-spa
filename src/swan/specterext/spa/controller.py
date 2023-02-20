import logging
import os
from flask import redirect, render_template, request, url_for, flash
from flask import current_app as app
from flask_login import login_required, current_user

from cryptoadvance.specter.specter import Specter
from cryptoadvance.specter.services.controller import user_secret_decrypted_required
from cryptoadvance.specter.user import User
from cryptoadvance.specter.wallet import Wallet
from .service import SpaService
from flask import send_from_directory
from graphql_server.flask import GraphQLView
import graphene

logger = logging.getLogger(__name__)

spa_endpoint = SpaService.blueprint
app.csrf.exempt(spa_endpoint)

def ext() -> SpaService:
    ''' convenience for getting the extension-object'''
    return app.specter.ext["spa"]

def specter() -> Specter:
    ''' convenience for getting the specter-object'''
    return app.specter


@spa_endpoint.route("/")
def index():
    return render_template(
        "spa/index.jinja",
    )

@spa_endpoint.route("/app/<path:path>")
def react_app(path):
    print(os.getcwd())
    print(os.path.join(os.getcwd(), 'build'))
    return send_from_directory(os.path.join(os.getcwd(), 'build'), path)


@spa_endpoint.route("/transactions")
@login_required
def transactions():
    # The wallet currently configured for ongoing autowithdrawals
    wallet: Wallet = SpaService.get_associated_wallet()

    return render_template(
        "spa/transactions.jinja",
        wallet=wallet,
        services=app.specter.service_manager.services,
    )


@spa_endpoint.route("/settings", methods=["GET"])
@login_required
@user_secret_decrypted_required
def settings_get():
    associated_wallet: Wallet = SpaService.get_associated_wallet()

    # Get the user's Wallet objs, sorted by Wallet.name
    wallet_names = sorted(current_user.wallet_manager.wallets.keys())
    wallets = [current_user.wallet_manager.wallets[name] for name in wallet_names]

    return render_template(
        "spa/settings.jinja",
        associated_wallet=associated_wallet,
        wallets=wallets,
        cookies=request.cookies,
    )

@spa_endpoint.route("/settings", methods=["POST"])
@login_required
@user_secret_decrypted_required
def settings_post():
    show_menu = request.form["show_menu"]
    user = app.specter.user_manager.get_user()
    if show_menu == "yes":
        user.add_service(SpaService.id)
    else:
        user.remove_service(SpaService.id)
    used_wallet_alias = request.form.get("used_wallet")
    if used_wallet_alias != None:
        wallet = current_user.wallet_manager.get_by_alias(used_wallet_alias)
        SpaService.set_associated_wallet(wallet)
    return redirect(url_for(f"{ SpaService.get_blueprint_name()}.settings_get"))
