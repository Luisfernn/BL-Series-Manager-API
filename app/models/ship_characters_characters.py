from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class ShipCharacterCharacter(Base):
    __tablename__ = "ship_characters_characters"

    ship_id = Column(ForeignKey("ship_characters.id"), Integer, nullable=False, unique=True)
    character_id = Column(ForeignKey("characters.id"), Integer, nullable=False, unique=True)
