from pydantic import Field
from src.models.Schedule.Schedule import Schedule


class CreateSchedule(Schedule):
    id: int = Field(exclude=True)
    