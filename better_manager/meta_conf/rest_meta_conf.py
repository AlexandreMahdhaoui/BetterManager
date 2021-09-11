class RestMetaConf:
    name = 'rest'
    type = 'better_rest'
    graph = {
        'provider': 'graph'
    },
    services = {
        'provider': 'services'
    }

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
