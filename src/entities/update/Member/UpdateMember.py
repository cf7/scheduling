from pydantic import Field
from models.Member.Member import Member


class UpdateMember(Member):
    id: int = Field(exclude=True)
