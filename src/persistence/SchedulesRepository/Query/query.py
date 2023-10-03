from entities.models.Schedule.Schedule import Schedule


class ScheduleQuery:
    def __init__():
        ...

    @staticmethod
    def get_schedules(schedule_ids: List[int]) -> List[Schedule]:
        return [
            Schedule(
                id=1,
                name="Test Get Schedule",
                timezone="America/Los_Angeles",
                url="https://example.com/schedule?id=1",
            )
        ]
