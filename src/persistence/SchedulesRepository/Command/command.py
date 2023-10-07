from typing import List
from entities.create.Schedule.CreateSchedule import CreateSchedule
from entities.models.Schedule.Schedule import Schedule
from entities.update.Schedule.UpdateSchedule import UpdateSchedule

"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


class ScheduleCommand:
    @staticmethod
    def create_schedules(create_schedules: List[CreateSchedule]) -> List[Schedule]:
        # access DB and mutate data
        print("create_schedules command")
        return [
            Schedule(
                id=1,
                name="Created Schedule",
                timezone="America/Los_Angeles",
                url="https://example.com/schedule?id=1",
            )
        ]

    @staticmethod
    def update_schedules(update_schedules: List[UpdateSchedule]) -> List[Schedule]:
        # access DB and mutate data
        print("update_schedules command")
        return [
            Schedule(
                id=1,
                name="Created Schedule",
                timezone="America/Los_Angeles",
                url="https://example.com/schedule?id=1",
            )
        ]
