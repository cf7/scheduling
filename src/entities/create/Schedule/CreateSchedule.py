from pydantic import Field
from entities.models.Schedule.Schedule import Schedule


class CreateSchedule(Schedule):
    id: int = Field(exclude=True)
