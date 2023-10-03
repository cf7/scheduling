from models.create.Member.CreateMember import CreateMember
from models.update.Member.UpdateMember import UpdateMember
from models.entities.Member.Member import Member


class MembersQuery:
    def __init__(self):
        pass

    @staticmethod
    def get_members(member_ids: List[int]) -> List[Member]:
        return None
