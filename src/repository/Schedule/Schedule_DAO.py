from models.create.Schedule.CreateSchedule import CreateSchedule
from models.update.Schedule.UpdateSchedule import UpdateSchedule
from models.entities.Schedule.Schedule import Schedule

"""
Repository layer is usually considered closer
to the Domain (i.e. the business logic / concepts / entities)
Respoitories implement DAO's, but no the other way around

DAO layer is usually considered closer
to the data persistence layer (DB)
(it doesn't necessarily have to be 1-to-1 per table,
especially since you'd want to be able to swap out
persistence layers as well)
"""


class Schedule_DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_schedule(schedule_id: int) -> Schedule:
        # mock schedule entity
        return Schedule(
            id=1,
            name="Test Schedule",
            timezone="America/Los_Angeles",
            url="https://example.com/schedule?id=1",
        )

    @staticmethod
    def create_schedule(create_schedule: CreateSchedule) -> Schedule:
        return None

    @staticmethod
    def update_schedule(update_schedule: UpdateSchedule) -> Schedule:
        return None
