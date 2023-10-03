from enum import Enum
from service.Member.MemberService import MemberService
from service.Schedule.ScheduleService import ScheduleService


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
        "/schedules/{schedule_id}": ScheduleService.get_schedule,
    },
    "POST": {
        "/schedules": ScheduleService.create_schedules,
        "/members": MemberService.create_members,
    },
    "PUT": {"/slots": lambda x: x},
    "DELETE": {},
}

"""
Design Decision
- always make endpoints bulk operations to future proof
"""
