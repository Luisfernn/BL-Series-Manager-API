from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class ShipActorsActors(Base):
    __tablename__ = "ship_actors_actors"

    ship_actor_id = Column(Integer, ForeignKey("ship_actors.id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)