"""
Here Configuration of your Extension takes place
"""


class BaseConfig:
    ''' This is a extension-based Config which is used as Base '''
    SPA_SOMEKEY = "some value"

class ProductionConfig(BaseConfig):
    ''' This is a extension-based Config for Production '''
    pass

