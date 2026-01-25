from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    series_id = Column(ForeignKey("series.id"), Integer)
    actor_id = Column(ForeignKey("actors.id"), Integer)
    role_type = Column(String, nullable=False)
