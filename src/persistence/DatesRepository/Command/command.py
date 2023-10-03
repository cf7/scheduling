from models.create.Member.CreateMember import CreateMember
from models.update.Member.UpdateMember import UpdateMember
from models.entities.Member.Member import Member


class DatesQuery:
    def __init__(self):
        ...

    @staticmethod
    def create_member(create_member: CreateMember) -> Member:
        return None

    @staticmethod
    def update_member(update_member: UpdateMember) -> Member:
        return None
