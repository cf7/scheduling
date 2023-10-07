from typing import List
from entities.create.Slot.CreateSlot import CreateSlot
from entities.models.Member.Member import Member
from entities.models.Slot.Slot import Slot
from entities.update.Slot.UpdateSlot import UpdateSlot


class SlotsCommand:
    def __init__(self):
        ...

    @staticmethod
    def create_slots(create_slots: List[CreateSlot]) -> Member:
        return Slot(id=1)

    @staticmethod
    def update_slots(update_slots: List[UpdateSlot]) -> Member:
        return Slot(id=1)
