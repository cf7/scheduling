from typing import List

from entities.models.Date.Date import Date


class DatesQuery:
    def __init__(self):
        ...

    @staticmethod
    def get_dates(date_ids: List[int]) -> List[Date]:
        return [Date(id=1, schedule_id=1, date="")]
