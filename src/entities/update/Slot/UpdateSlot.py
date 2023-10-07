from pydantic import Field
from entities.models.Slot.Slot import Slot


class UpdateSlot(Slot):
    id: int = Field(exclude=True)
