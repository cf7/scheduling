"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


from entities.create.Member.CreateMember import CreateMember
from entities.models.Member.Member import Member
from entities.update.Member.UpdateMember import UpdateMember
from persistence.MembersRepository.MembersRepository import MembersRepository


class MemberService:
    @staticmethod
    def get_member(member_ids: int) -> Member:
        return MembersRepository.get_members(member_ids)

    @staticmethod
    def create_member(create_members: CreateMember) -> Member:
        # handle business logic here
        # . . .
        return MembersRepository.create_members(create_members)

    @staticmethod
    def update_member(update_members: UpdateMember) -> Member:
        return MembersRepository.update_members(update_members)
