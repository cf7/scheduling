from typing import List

from entities.create.Member.CreateMember import CreateMember
from entities.models.Member.Member import Member
from entities.update.Member.UpdateMember import UpdateMember


class MembersCommand:
    def __init__(self):
        ...

    @staticmethod
    def create_members(create_members: List[CreateMember]) -> Member:
        return Member(id=1, name="test user", schedule_id=1, slot_ids=[])

    @staticmethod
    def update_members(update_members: List[UpdateMember]) -> Member:
        return Member(id=1, name="test user", schedule_id=1, slot_ids=[])
