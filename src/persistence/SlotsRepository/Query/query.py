from typing import List

from entities.models.Member.Member import Member
from entities.models.Slot.Slot import Slot


class SlotsQuery:
    def __init__(self):
        ...

    @staticmethod
    def get_slots(slot_ids: List[int]) -> List[Slot]:
        return [Slot(id=1, date_id=1)]
