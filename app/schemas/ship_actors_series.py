from pydantic import BaseModel


class ShipActorsSeriesCreate(BaseModel):
    ship_id: int


class ShipActorsByNameCreate(BaseModel):
    ship_name: str
    actor1_nickname: str
    actor2_nickname: str