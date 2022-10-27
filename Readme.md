

```
# Flask part
git clone git@github.com:cryptoadvance/specterext-spa.git
cd specterext-spa
virtualenv --python=python3 .env
. ./.env/bin/activate
pip3 install -r requirements.txt
pip3 install -e .

# npm part
npm i
npm run build

python3 -m cryptoadvance.specter server --config DevelopmentConfig --debug

# point your browser to:
# http://localhost:25441/svc/spa/app
# We'll later make this the default link ...
```
