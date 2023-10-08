from pydantic import Field
from entities.models.Member.Member import Member


class CreateMember(Member):
    id: int = Field(exclude=True)
