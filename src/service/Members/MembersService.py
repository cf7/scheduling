from repository.member.member_DAO import member_DAO
from models.create.member.Createmember import Createmember
from models.entities.member.member import member

"""
Connect Service Layer to Repository Layer

Business logic and orchestration layer that implements 
high-level CRUD functionality over entities.

Verifies that the requester has correct permissions (read or write)
and then delegates access to the repository layer.
"""


class MemberService:
    @staticmethod
    def get_member(member_id: int) -> member:
        print("member_id: ", member_id)
        return None

    @staticmethod
    def create_member(create_member: Createmember) -> member:
        # handle business logic here
        # . . .

        return None
