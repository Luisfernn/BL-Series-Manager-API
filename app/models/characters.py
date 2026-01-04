from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Associações opcionais (decisão consciente)
    series_id = Column(Integer, ForeignKey("series.id"), nullable=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=True)