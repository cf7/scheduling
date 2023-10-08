from datetime import datetime
from pydantic import BaseModel, StrictInt


class Date(BaseModel):
    id: StrictInt
    date: datetime
    schedule_id: int

    @staticmethod
    def get_instance(default=None):
        if default is None:
            default = {}
        return Date(**default)
