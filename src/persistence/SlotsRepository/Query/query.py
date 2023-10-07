from typing import List

from entities.models.Member.Member import Member
from entities.models.Slot.Slot import Slot


class SlotsQuery:
    def __init__(self):
        ...

    @staticmethod
    def get_slots(slot_ids: List[int]) -> Member:
        return Slot(id=1)
