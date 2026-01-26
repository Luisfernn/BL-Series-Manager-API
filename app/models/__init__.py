# Import all models to register them with SQLAlchemy
from app.models.base import Base
from app.models.actors import Actor
from app.models.series import Series
from app.models.characters import Character
from app.models.tags import Tag
from app.models.ship_actors import ShipActor
from app.models.ship_characters import ShipCharacter

# Association tables
from app.models.series_actors import SeriesActor
from app.models.series_tag import SeriesTag
from app.models.series_characters import SeriesCharacter
from app.models.ship_actors_actors import ShipActorActor
from app.models.ship_actors_series import ShipActorSeries
from app.models.ship_characters_characters import ShipCharacterCharacter

__all__ = [
    "Base",
    "Actor",
    "Series",
    "Character",
    "Tag",
    "ShipActor",
    "ShipCharacter",
    "SeriesActor",
    "SeriesTag",
    "SeriesCharacter",
    "ShipActorActor",
    "ShipActorSeries",
    "ShipCharacterCharacter",
]
