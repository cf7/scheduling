from enum import Enum

from service.ScheduleService import ScheduleService


"""
Connect Routing Layer to Service Layers

"""


class Endpoint:
    def __init__(self, url: str, handler: callable):
        self.url = url
        self.handler = handler


class HTTP_Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Request:
    def __init__(self, method: HTTP_Method, handler: callable):
        self.method = method


route_factory = {
    "GET": {
        "/schedule/{schedule_id}": ScheduleService.get_schedule,
    },
    "POST": {"/schedule": ScheduleService.create_schedule},
    "PUT": {},
    "DELETE": {},
}
