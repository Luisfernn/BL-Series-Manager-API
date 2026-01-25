from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipActorActor(Base):
    __tablename__ = "ship_actors_actors"

    ship_id = Column(Integer, ForeignKey("ship_actors.id"), nullable=False, primary_key=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=False, primary_key=True)
