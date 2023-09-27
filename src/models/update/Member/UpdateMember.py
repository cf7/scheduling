from pydantic import Field
from models.entities.Member.Member import Member


class UpdateMember(Member):
    id: int = Field(exclude=True)
