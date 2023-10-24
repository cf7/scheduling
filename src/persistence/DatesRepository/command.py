from datetime import datetime
from typing import List
from entities.create.Date.CreateDate import CreateDate
from entities.update.Date.UpdateDate import UpdateDate
from entities.models.Date.Date import Date


class DatesCommand:
    def __init__(self):
        ...

    @staticmethod
    def create_dates(create_dates: List[CreateDate]) -> List[Date]:
        print("create_dates command")
        return [Date(id=1, schedule_id=1, date=datetime.now())]

    @staticmethod
    def update_dates(update_dates: List[UpdateDate]) -> List[Date]:
        return [Date(id=1, schedule_id=1, date=datetime.now())]
