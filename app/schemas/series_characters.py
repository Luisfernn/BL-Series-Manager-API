from pydantic import BaseModel
from typing import List


class SeriesCharactersAdd(BaseModel):
    character_ids: List[int]