from pydantic import Field

from entities.models.Date.Date import Date


class CreateDate(Date):
    id: int = Field(exclude=True)
