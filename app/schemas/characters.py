from pydantic import BaseModel, Field
from typing import Optional


class CharacterBase(BaseModel):
    name: str = Field(..., example="Kim Min-gyu")
    role_type: str = Field(..., example="Main", description="Tipo de papel: Main, Support, etc")


class CharacterCreate(CharacterBase):
    series_id: int = Field(..., example=1)
    actor_id: Optional[int] = Field(None, example=1)


class CharacterUpdate(BaseModel):
    """Schema para atualização de personagem - todos os campos são opcionais"""
    name: Optional[str] = Field(None, example="Kim Min-gyu")
    series_id: Optional[int] = Field(None, example=1)
    actor_id: Optional[int] = Field(None, example=1)
    role_type: Optional[str] = Field(None, example="Main")


class CharacterResponse(CharacterBase):
    id: int
    series_id: int
    actor_id: Optional[int] = None

    class Config:
        from_attributes = True