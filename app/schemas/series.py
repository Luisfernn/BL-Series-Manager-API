from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal
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


class SeriesUpdate(BaseModel):
    """Schema para atualização de série - todos os campos são opcionais"""
    title: Optional[str] = Field(None, example="Love in the Moonlight")
    country: Optional[str] = Field(None, example="Thailand")
    release_date: Optional[date] = Field(None, example="2023-08-15")
    episode_number: Optional[int] = Field(None, example="12")
    genre: Optional[str] = Field(None, example="Romance, Drama")
    synopsis: Optional[str] = Field(None, example="A story about...")
    platform: Optional[str] = Field(None, example="Netflix")
    rate: Optional[Decimal] = Field(None, example=8.5, ge=0, le=10)
    status: Optional[Literal["Completed", "Dropped"]] = Field(None, example="Completed")
    production_company: Optional[str] = Field(None, example="GMMTV")
    date_start: Optional[date] = Field(None, example="2023-08-15")
    date_watched: Optional[date] = Field(None, example="2023-09-20")


class SeriesResponse(SeriesBase):
    id: int

    class Config:
        from_attributes = True