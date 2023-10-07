from typing import List
from entities.create.Slot.CreateSlot import CreateSlot
from entities.models.Slot.Slot import Slot
from entities.update.Slot.UpdateSlot import UpdateSlot
from persistence.SlotsRepository.Command.command import SlotsCommand
from persistence.SlotsRepository.Query.query import SlotsQuery


class SlotsRepository:
    def __init__():
        # constructor - not mandatory
        # initializes instance attributes
        ...

    @staticmethod
    def get_slots(slot_ids: List[int]) -> List[Slot]:
        return SlotsQuery.get_slots(slot_ids)

    @staticmethod
    def create_slots(create_slots: List[CreateSlot]) -> List[Slot]:
        return SlotsCommand.create_slots(create_slots)

    @staticmethod
    def update_slots(update_slots: List[UpdateSlot]) -> List[Slot]:
        return SlotsCommand.update_slots(update_slots)
