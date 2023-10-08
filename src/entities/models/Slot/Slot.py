from pydantic import BaseModel, StrictInt
from datetime import datetime


class Slot(BaseModel):
    id: StrictInt
    date_id: int
    start_time: datetime
    end_time: datetime
