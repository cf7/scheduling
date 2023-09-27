from pydantic import Field
from models.entities.Member.Member import Member


class CreateMember(Member):
    id: int = Field(exclude=True)
