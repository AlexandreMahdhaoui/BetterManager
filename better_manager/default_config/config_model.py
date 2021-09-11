from pydantic import BaseModel


class ConfigBaseModel(BaseModel):

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}


class DbConf(BaseModel):
    db_type: str
    cnx_str: str
    db_name: str
    db_collection: str
