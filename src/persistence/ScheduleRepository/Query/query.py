from entities.models.Schedule.Schedule import Schedule


class ScheduleQuery:
    def __init__():
        ...

    """
    implement DAO's here
    """

    @staticmethod
    def get_schedule(schedule_id: int) -> Schedule:
        return Schedule(
            id=1,
            name="Test Get Schedule",
            timezone="America/Los_Angeles",
            url="https://example.com/schedule?id=1",
        )
