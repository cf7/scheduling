from pydantic import BaseModel

class Date(BaseModel):
    date: str
    schedule_id: int
    