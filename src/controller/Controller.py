class Controller:
    
    def __init__(self, endpoint_factory):
        self.endpoint_factory = endpoint_factory
    
    @classmethod
    def get_instance(cls, endpoint_factory):
        return cls(endpoint_factory)
    
    
    @staticmethod
    def controller_action(event):

        return {}