from pydantic import Field
from models.entities.Schedule.Schedule import Schedule


class UpdateSchedule(Schedule):
    id: int = Field(exclude=True)
