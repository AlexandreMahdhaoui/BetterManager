from abc import ABC

from better_base.better_base import BetterBase
from better_manager.default_config.base_default_config import BaseDefaultConfig
from better_manager.default_config.graph_default_config import GraphDefaultConfig
from better_manager.default_config.rest_default_config import RestDefaultConfig
from better_manager.default_config.services_default_config import ServicesDefaultConfig
from better_manager.meta_conf.base_meta_conf import BaseMetaConf
from better_manager.meta_conf.graph_meta_conf import GraphMetaConf
from better_manager.meta_conf.rest_meta_conf import RestMetaConf
from better_manager.meta_conf.services_meta_conf import ServicesMetaConf


class BetterManager(ABC):
    """
    Usage:
        Provides a super class for AppManager's class that can read their default_config from DB, YAML, JSON or ENV variables \
        and programmatically creates following microservices libraries (sorted by chronological initialization): \n
        > BetterBase, BetterFiles, BetterAuth, BetterGraph, BetterServices, BetterLogs, BetterRest,  \n

            Please note that BetterBase bootstraps everything because most of the default_config come from database.  \n
        BetterManager also provides administration interfaces for those microservices: CREATE/UPDATE/DELETE \n

    Meta Config:
        To bootstrap AppManager and resolve interoperability, the AppManager has to specify the meta configuration of \
        each microservices
        \n
        -> Unless SyncBetter decides to store customer's meta configurations and provides an adapter; Meta default_config \
        can't directly come from a database because its adapters hasn't been yet configured.

    Example:
        >>> class AppManager(BetterManager):
                 name = "SyncBetter"
                 better_graph = BetterGraphMetaConfigSubClass
                 better_services = "/better_services_meta_config.json"
                 better_rest = "./better_rest_meta_config.yaml"
                 better_logs = meta_config_dict
            AppManager.init(config_new_app=True)
            app = Starlette(
                debug=True,
                routes=AppManager.routes)
    """
    name: str  # Name of the App << eg SyncBetter

    _prohibited_keys = ['name', 'init']
    _namespace: dict
    _microservices = ('base', 'files', 'auth', 'graph', 'services', 'logs', 'rest')
    _class_tuple = (
        BaseMetaConf,
        # BetterFilesMetaConfig,
        # BetterAuthMetaConfig,
        GraphMetaConf,
        ServicesMetaConf,
        # BetterLogsMetaConfig
        RestMetaConf,
    )

    @property
    def routes(self):
        return self._namespace['rest'].routes

    @classmethod
    def init(cls, config_new_app=False):
        cls._init_namespace_from_meta_conf()
        cls._init_base()
        if config_new_app:
            cls._config_new_app()
        cls._bootstrap()

    @classmethod
    def _bootstrap(cls):
        cls._namespace['base']['instance'].bootstrap()
        microservices = cls._get_microservices()
        for k, v in microservices.items():
            if k == 'base':
                v.init()  # BetterBase's initialization called after the config bootstrapping process
            v['instance'].__init__(k, cls._namespace)
        pass

    @classmethod
    def _init_namespace_from_meta_conf(cls):
        for meta_conf in cls._list_meta_conf():
            cls._namespace[meta_conf['name']] = dict()
            cls._namespace[meta_conf['name']]['meta_conf'] = meta_conf
            cls._namespace[meta_conf['name']]['config'] = dict()

    @classmethod
    def _init_base(cls):
        cls._namespace['base']['instance'] = BetterBase(name='base', namespace=cls._namespace)

    @classmethod
    def _get_microservices(cls):
        return {m: cls._namespace[m] for m in cls._microservices if m in cls._namespace}

    @classmethod
    def _list_meta_conf(cls):
        return [cls._sanitize_meta_dict(v) for k, v in cls.__dict__.items()
                if not k.startswith('_') and k not in cls._prohibited_keys]

    @classmethod
    def _config_new_app(cls):
        # cls._config_new_app creates the configuration for a default app
        base = BaseDefaultConfig.to_dict()
        graph = GraphDefaultConfig.to_dict()
        services = ServicesDefaultConfig.to_dict()
        rest = RestDefaultConfig.to_dict()
        cls._namespace['base']['instance'].config_new_app(base, graph, services, rest)

    @classmethod
    def _sanitize_meta_dict(cls, v):
        if isinstance(v, dict):  # Means it's already a dictionary meta default_config
            return v
        if isinstance(v, str):  # Means it's a .json or .yaml default_config file
            if v.endswith('.json'):
                return cls._json_to_dict(v)
            if v.endswith('.yaml'):
                return cls._yaml_to_dict(v)
        if issubclass(v, cls._class_tuple):  # Means it's a subclass of a MetaConfig
            return v.to_dict()

    @classmethod
    def _json_to_dict(cls, v):
        with open(v) as json:
            pass

    @classmethod
    def _yaml_to_dict(cls, v):
        with open(v) as yaml:
            pass
