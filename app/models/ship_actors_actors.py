from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class ShipActorActor(Base):
    __tablename__ = "ship_actors_actors"

    ship_id = Column(ForeignKey("ship_actors.id"), Integer, nullable=False, unique=True)
    actor_id = Column(ForeignKey("actors.id"), Integer, nullable=False, unique=True)
