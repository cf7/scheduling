from pydantic import BaseModel, StrictInt
from typing import List


class Member(BaseModel):
    id: StrictInt
    name: str
    schedule_id: int
    slot_ids: List[int]
