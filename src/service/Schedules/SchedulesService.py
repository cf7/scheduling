from persistence.ScheduleRepository.ScheduleRepository import ScheduleRepository
from entities.create.Schedule.CreateSchedule import CreateSchedule
from entities.models.Schedule.Schedule import Schedule

"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


class ScheduleService:
    @staticmethod
    def get_schedules(schedule_ids: List[int]) -> List[Schedule]:
        print("schedule_id: ", schedule_ids)
        return ScheduleRepository.get_schedules(schedule_ids)

    @staticmethod
    def create_schedules(create_schedules: List[CreateSchedule]) -> List[Schedule]:
        # always make calls bulk operations first to future proof

        # handle business logic here
        # . . .

        # create schedule
        # create dates
        # create slots (using start time and end time constraints)

        schedule = ScheduleRepository.create_schedules(create_schedules)

        return None
