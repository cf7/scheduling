from pydantic import Field
from entities.models.Schedule.Schedule import Schedule


class UpdateSchedule(Schedule):
    id: int = Field(exclude=True)
