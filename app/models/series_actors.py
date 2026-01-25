from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class SeriesActor(Base):
    __tablename__ = "series_actors"

    series_id = Column(ForeignKey("series.id"), Integer, primary_key=True, unique=True)
    actor_id = Column(ForeignKey("actors.id"), Integer, primary_key=True, unique=True)
