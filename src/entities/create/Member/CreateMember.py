from pydantic import Field
from models.Member.Member import Member


class CreateMember(Member):
    id: int = Field(exclude=True)
