from pydantic import BaseModel


class ActorBase(BaseModel):
    name: str


class ActorCreate(ActorBase):
    pass


class ActorResponse(ActorBase):
    id: int

    class Config:
        from_attributes = True