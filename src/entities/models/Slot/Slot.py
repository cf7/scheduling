from pydantic import BaseModel
from datetime import datetime

class Slot(BaseModel):
    date_id: int
    start_time: datetime
    end_time: datetime


