from datetime import datetime
from typing import List

from entities.create.Date.CreateDate import CreateDate
from entities.create.Schedule.CreateSchedule import CreateSchedule
from entities.create.Slot.CreateSlot import CreateSlot
from entities.models.Schedule.Schedule import Schedule
from persistence.DatesRepository.DatesRepository import DatesRepository
from persistence.SchedulesRepository.SchedulesRepository import SchedulesRepository
from persistence.SlotsRepository.SlotsRepository import SlotsRepository

"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


class SchedulesService:
    @staticmethod
    def get_schedules(schedule_ids: List[int]) -> List[Schedule]:
        print("schedule_id: ", schedule_ids)
        return SchedulesRepository.get_schedules(schedule_ids)

    @staticmethod
    def create_schedules(create_schedules: List[CreateSchedule]) -> List[Schedule]:
        print("create_schedules service")
        # always make calls bulk operations first to future proof

        # handle business logic here
        # . . .

        # create schedule
        # create dates
        # create slots (using start time and end time constraints)

        schedules = SchedulesRepository.create_schedules(create_schedules)
        schedules_map = {sch.id: sch for sch in schedules}

        print("schedules created successfully")

        dates = DatesRepository.create_dates(
            [CreateDate(schedule_id=sch.id, date=datetime.now()) for sch in schedules]
        )
        print("dates created successfully: ", dates)
        dates_by_schedule = {d.schedule_id: d for d in dates}

        print("dates map: ", dates_by_schedule)

        slots = []
        # need to group slots by date because start/end time constraint determined
        # per schedule, which dates are tied to
        for schedule_id in dates_by_schedule.keys():
            schedule = schedules_map.get(schedule_id)
            slots = SlotsRepository.create_slots(
                [
                    CreateSlot(
                        date_id=date.id,
                        start_time=datetime.now(),  # schedule.start_time_constraint,
                        end_time=datetime.now(),  # schedule.end_time_constraint,
                    )
                    for date in dates
                ],
            )

        return {"schedules": schedules, "dates": dates, "slots": slots}
