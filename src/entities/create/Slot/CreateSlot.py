from pydantic import Field

from entities.models.Slot.Slot import Slot


class CreateSlot(Slot):
    id: int = Field(exclude=True)
