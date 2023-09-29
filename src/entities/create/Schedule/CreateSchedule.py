from pydantic import Field
from models.entities.Schedule.Schedule import Schedule


class CreateSchedule(Schedule):
    id: int = Field(exclude=True)
