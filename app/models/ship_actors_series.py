from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class ShipActorSeries(Base):
    __tablename__ = "ship_actors_series"

    id = Column(Integer, primary_key=True)
    ship_id = Column(ForeignKey("ship_actors.id"), Integer, nullable=False, unique=True)
    series_id = Column(ForeignKey("series.id"), Integer, nullable=False, unique=True)
