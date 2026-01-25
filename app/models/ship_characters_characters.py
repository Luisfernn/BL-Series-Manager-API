from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipCharacterCharacter(Base):
    __tablename__ = "ship_characters_characters"

    ship_id = Column(Integer, ForeignKey("ship_characters.id"), nullable=False, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False, primary_key=True)
