from pydantic import BaseModel, Optional

class Schedule(BaseModel):
    name: str
    timezone: str
    url: str

    start_time_constraint: Optional[str]
    end_time_constraint: Optional[str]