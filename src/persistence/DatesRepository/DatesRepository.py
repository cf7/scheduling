from typing import List
from entities.create.Date.CreateDate import CreateDate
from entities.models.Date.Date import Date
from entities.update.Date.UpdateDate import UpdateDate
from persistence.DatesRepository.Command.command import DatesCommand
from persistence.DatesRepository.Query.query import DatesQuery


class DatesRepository:
    def __init__():
        # constructor - not mandatory
        # initializes instance attributes
        ...

    @staticmethod
    def get_dates(date_ids: List[int]) -> List[Date]:
        return DatesQuery.get_dates(date_ids)

    @staticmethod
    def create_dates(create_dates: List[CreateDate]) -> List[Date]:
        return DatesCommand.create_dates(create_dates)

    @staticmethod
    def update_dates(update_dates: List[UpdateDate]) -> List[Date]:
        return DatesCommand.update_dates(update_dates)
