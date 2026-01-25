from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ActorBase(BaseModel):
    name: str = Field(..., example="Park Seo-joon")
    nickname: str = Field(..., example="Seo-joon")
    nationality: str = Field(..., example="South Korea")
    gender: str = Field(..., example="M")


class ActorCreate(ActorBase):
    birthday: Optional[date] = Field(None, example="1988-12-16")
    agency: Optional[str] = Field(None, example="Awesome ENT")
    ig: Optional[str] = Field(None, example="@actorparkseojun")


class ActorResponse(ActorBase):
    id: int
    birthday: Optional[date] = None
    agency: Optional[str] = None
    ig: Optional[str] = None

    class Config:
        from_attributes = True