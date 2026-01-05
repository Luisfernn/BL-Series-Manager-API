from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipCharactersCharacters(Base):
    __tablename__ = "ship_characters_characters"

    ship_character_id = Column(Integer, ForeignKey("ship_characters.id"), primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)