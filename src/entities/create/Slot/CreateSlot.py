from pydantic import BaseModel, StrictInt
from datetime import datetime


class CreateSlot(BaseModel):
    date_id: StrictInt
    start_time: datetime
    end_time: datetime
