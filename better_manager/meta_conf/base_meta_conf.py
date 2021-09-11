from os import getenv

from better_base.utils.subscriptable_class import Subscriptable


class BaseMetaConf(Subscriptable):
    name = 'base'
    type = 'better_base'
    bootstrap = {
        'db_type': getenv('DB_TYPE'),
        'cnx_str': getenv('CNX_STR'),
        'db_name': getenv('DB_NAME'),
        'db_collection': 'default_config'
    }

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
