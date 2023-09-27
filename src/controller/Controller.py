from routes.Routes import HTTP_Method


class Controller:
    def __init__(self, route_factory):
        self.route_factory = route_factory

    @classmethod
    def get_instance(cls, route_factory):
        return cls(route_factory)

    def get_handler(self, http_method: HTTP_Method, resource_path: str):
        handlers_by_method = self.route_factory.get(http_method)
        return handlers_by_method.get(resource_path)

    def controller_action(self, event):
        http_method = event.get("httpMethod")
        resource_path = event.get("requestContext").get("resourcePath")
        print("method: ", http_method)
        print("resource_path1: ", resource_path)

        handler = None
        if http_method:
            handler = self.get_handler(http_method, resource_path)

        handler(1)

        return {}
