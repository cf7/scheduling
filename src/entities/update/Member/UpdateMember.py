from pydantic import Field
from entities.models.Member.Member import Member


class UpdateMember(Member):
    id: int = Field(exclude=True)
