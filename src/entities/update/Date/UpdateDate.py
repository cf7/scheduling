from pydantic import Field
from entities.models.Date.Date import Date


class UpdateDate(Date):
    id: int = Field(exclude=True)
