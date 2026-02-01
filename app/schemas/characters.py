from pydantic import BaseModel, Field
from typing import Optional


class CharacterBase(BaseModel):
    name: str = Field(..., example="Kim Min-gyu")
    role_type: str = Field(..., example="Main", description="Tipo de papel: Main, Support, etc")


class CharacterCreate(CharacterBase):
    series_id: int = Field(..., example=1)
    actor_nickname: str = Field(..., example="Bright", description="Nickname do ator/atriz que interpreta o personagem")


class CharacterResponse(CharacterBase):
    id: int
    series_id: int
    actor_id: Optional[int] = None

    class Config:
        from_attributes = True