from repository.Schedule.Schedule_DAO import Schedule_DAO
from models.create.Schedule.CreateSchedule import CreateSchedule
from models.entities.Schedule.Schedule import Schedule

"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


class ScheduleService:
    @staticmethod
    def get_schedule(schedule_id: int) -> Schedule:
        print("schedule_id: ", schedule_id)
        return Schedule_DAO.get_schedule(schedule_id)

    @staticmethod
    def create_schedule(create_schedule: CreateSchedule) -> Schedule:
        # handle business logic here
        # . . .

        return Schedule_DAO.create_schedule(create_schedule)
