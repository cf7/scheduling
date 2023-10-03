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
