from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal, List
from datetime import date
from decimal import Decimal


class SeriesBase(BaseModel):
    title: str = Field(..., example="Love in the Moonlight")
    country: str = Field(..., example="Thailand")
    release_date: date = Field(..., example="2023-08-15")
    episode_number: int = Field(..., example="12")
    genre: str = Field(..., example="Romance, Drama")
    synopsis: str = Field(..., example="A story about...")
    platform: str = Field(..., example="Netflix")
    rate: Decimal = Field(..., example=8.5, ge=0, le=10)

    # Campos opcionais
    status: Optional[Literal["Completed", "Dropped"]] = Field(
        None,
        example="Completed",
        description="Status da série: 'Completed' ou 'Dropped'"
    )
    production_company: Optional[str] = Field(None, example="GMMTV")
    date_start: Optional[date] = Field(None, example="2023-08-15")
    date_watched: Optional[date] = Field(None, example="2023-09-20")


class SeriesCreate(SeriesBase):
    pass


class SeriesResponse(SeriesBase):
    id: int

    class Config:
        from_attributes = True


class ActorInSeries(BaseModel):
    id: int
    name: str
    birthday: Optional[date] = None
    agency: Optional[str] = None
    ig: Optional[str] = None

    class Config:
        from_attributes = True


class CharacterInSeries(BaseModel):
    id: int
    name: str
    role_type: str
    actor_id: Optional[int] = None

    class Config:
        from_attributes = True


class TagInSeries(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ShipActorInSeries(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ShipCharacterInSeries(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class SeriesDetailResponse(SeriesBase):
    id: int
    actors: List[ActorInSeries] = []
    characters: List[CharacterInSeries] = []
    tags: List[TagInSeries] = []
    ship_actors: List[ShipActorInSeries] = []
    ship_characters: List[ShipCharacterInSeries] = []

    class Config:
        from_attributes = True