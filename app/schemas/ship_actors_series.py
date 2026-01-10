from pydantic import BaseModel


class ShipActorsSeriesCreate(BaseModel):
    ship_id: int