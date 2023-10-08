from datetime import datetime
from pydantic import BaseModel, StrictInt


class CreateDate(BaseModel):
    schedule_id: StrictInt
    date: datetime
