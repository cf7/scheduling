from pydantic import BaseModel
from typing import List

class Member(BaseModel):
    name: str
    schedule_id: int
    slot_ids: List[int]
