from typing import List

from entities.models.Member.Member import Member


class MembersQuery:
    def __init__(self):
        pass

    @staticmethod
    def get_members(member_ids: List[int]) -> List[Member]:
        return Member(id=1, name="test user", schedule_id=1, slot_ids=[])
