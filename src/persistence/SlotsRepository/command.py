from typing import List
from datetime import datetime
from entities.create.Slot.CreateSlot import CreateSlot
from entities.models.Member.Member import Member
from entities.models.Slot.Slot import Slot
from entities.update.Slot.UpdateSlot import UpdateSlot


class SlotsCommand:
    def __init__(self):
        ...

    @staticmethod
    def create_slots(create_slots: List[CreateSlot]) -> List[Slot]:
        print("create slots command")
        return [
            Slot(id=1, date_id=1, start_time=datetime.now(), end_time=datetime.now())
        ]

    @staticmethod
    def update_slots(update_slots: List[UpdateSlot]) -> List[Slot]:
        return [
            Slot(id=1, date_id=1, start_time=datetime.now(), end_time=datetime.now())
        ]
