"""

API Layer responsible solely for
handling routing and returning responses
"""

"""
Design Decision:

- move away from class based Controllers (which are old)
and instead use Minimal API approach which is method based

- basically Minimal API's defines a map and injects route-specific
dependencies into each handler route to use to process the request

- this minimizes the number of services and resources being initialized
on each run

- hence, services also need to be split up to be domain-specific so
they can be provided separately to each route method
"""


from typing import Dict
from api.routes.Routes import HTTP_Method


class API:
    def __init__(self, route_factory: Dict[str, Dict[str, callable]]):
        self.route_factory = route_factory

    @classmethod
    def get_instance(cls, route_factory):
        return cls(route_factory)

    def get_handler(self, http_method: HTTP_Method, resource_path: str) -> callable:
        handlers_by_method = self.route_factory.get(http_method)
        return handlers_by_method.get(resource_path)

    def api_action(self, event):
        print("======== api_action")
        http_method = event.get("httpMethod")
        resource_path = event.get("requestContext").get("resourcePath")
        print("method: ", http_method)
        print("resource_path1: ", resource_path)

        handler = None
        if http_method:
            handler = self.get_handler(http_method, resource_path)

        handler(1)

        return {}
