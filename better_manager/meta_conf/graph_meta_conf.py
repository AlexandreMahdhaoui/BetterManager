class GraphMetaConf:
    name = 'graph'
    type = 'better_graph'
    better_base = {
        'provider': 'base',
        'namespace': name
    }

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}
