from pydantic import BaseModel, StrictInt
from typing import Optional


class Schedule(BaseModel):
    id: StrictInt
    name: str
    timezone: str
    url: str

    start_time_constraint: Optional[str]
    end_time_constraint: Optional[str]
