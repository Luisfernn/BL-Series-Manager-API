from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipActorsSeries(Base):
    __tablename__ = "ship_actors_series"

    ship_actor_id = Column(Integer, ForeignKey("ship_actors.id"), primary_key=True)
    series_id = Column(Integer, ForeignKey("series.id"), primary_key=True)