class ServicesMetaConf:
    name = 'services'
    type = 'better_services'
    base = {
        'provider': 'base'
    }

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
