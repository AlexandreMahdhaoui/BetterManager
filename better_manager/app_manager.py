from better_manager.better_manager import BetterManager
from better_manager.meta_conf.base_meta_conf import BaseMetaConf
from better_manager.meta_conf.graph_meta_conf import GraphMetaConf
from better_manager.meta_conf.rest_meta_conf import RestMetaConf
from better_manager.meta_conf.services_meta_conf import ServicesMetaConf


class AppManager(BetterManager):
    name = "SyncBetter"
    better_base = BaseMetaConf
    better_graph = GraphMetaConf
    better_services = ServicesMetaConf
    better_rest = RestMetaConf
