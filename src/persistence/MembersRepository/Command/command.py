from models.create.Member.CreateMember import CreateMember
from models.update.Member.UpdateMember import UpdateMember
from models.entities.Member.Member import Member


class MembersCommand:
    def __init__(self):
        ...

    @staticmethod
    def create_members(create_members: CreateMember) -> Member:
        return None

    @staticmethod
    def update_members(update_members: UpdateMember) -> Member:
        return None
