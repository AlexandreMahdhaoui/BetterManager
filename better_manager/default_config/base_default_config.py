from better_manager.default_config.config_model import ConfigBaseModel


class BaseDefaultConfig(ConfigBaseModel):
    """
    BetterBase's default configuration.
    Contains the default default_config to create every default namespace's element
    Should "configs" get initialized here ?
        -> Default configs are coming from better_manager/default_config/*_default_config.py
        -> We should be able to init them from Bootstrap.
        -> However is other defaults configs part of this default_config or independent, meaning each default_conf initialized
            in Bootstrap
    """
    graph = {
        'name': 'graph',
    }
    services = {
        'name': 'services',
    }
    rest = {
        'name': 'rest',
    }
    config = {
        'name': 'config',
    }


