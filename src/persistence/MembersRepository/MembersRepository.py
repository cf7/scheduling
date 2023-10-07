from typing import List
from entities.create.Member.CreateMember import CreateMember
from entities.models.Member.Member import Member
from entities.update.Member.UpdateMember import UpdateMember
from persistence.MembersRepository.Command.command import MembersCommand
from persistence.MembersRepository.Query.query import MembersQuery


class MembersRepository:
    def __init__():
        ...

    @staticmethod
    def get_members(member_ids: List[int]) -> List[Member]:
        return MembersQuery.get_members(member_ids)

    @staticmethod
    def create_members(create_members: List[CreateMember]) -> List[Member]:
        return MembersCommand.create_members(create_members)

    @staticmethod
    def update_members(update_members: List[UpdateMember]) -> List[Member]:
        return MembersCommand.update_members(update_members)
