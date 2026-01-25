from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipActorSeries(Base):
    __tablename__ = "ship_actors_series"

    id = Column(Integer, primary_key=True)
    ship_id = Column(Integer, ForeignKey("ship_actors.id"), nullable=False)
    series_id = Column(Integer, ForeignKey("series.id"), nullable=False)
