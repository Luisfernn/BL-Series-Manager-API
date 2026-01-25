from pydantic import BaseModel, Field
from typing import Optional


class TagBase(BaseModel):
    name: str = Field(..., example="Romance")


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    """Schema para atualização de tag"""
    name: Optional[str] = Field(None, example="Romance")


class TagResponse(TagBase):
    id: int

    class Config:
        from_attributes = True