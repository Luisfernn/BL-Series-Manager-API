from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.actors import ActorCreate, ActorResponse, ActorUpdate
from app.services.actor_service import create_actor, get_actor_by_id, update_actor, delete_actor

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.post(
    "",
    response_model=ActorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_actor_endpoint(
    actor_in: ActorCreate,
    db: Session = Depends(get_db),
):
    return create_actor(
        db,
        name=actor_in.name,
        nickname=actor_in.nickname,
        nationality=actor_in.nationality,
        gender=actor_in.gender,
        birthday=actor_in.birthday,
        agency=actor_in.agency,
        ig=actor_in.ig
    )


@router.get(
    "/{actor_id}",
    response_model=ActorResponse,
    status_code=status.HTTP_200_OK,
)
def get_actor_endpoint(
    actor_id: int,
    db: Session = Depends(get_db),
):
    actor = get_actor_by_id(db, actor_id)
    if not actor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Actor not found"
        )
    return actor


@router.put(
    "/{actor_id}",
    response_model=ActorResponse,
    status_code=status.HTTP_200_OK,
)
def update_actor_endpoint(
    actor_id: int,
    actor_in: ActorUpdate,
    db: Session = Depends(get_db),
):
    try:
        actor = update_actor(db, actor_id, actor_in)
        return actor
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.delete(
    "/{actor_id}",
    status_code=status.HTTP_200_OK,
)
def delete_actor_endpoint(
    actor_id: int,
    db: Session = Depends(get_db),
):
    try:
        delete_actor(db, actor_id)
        return {"message": "Actor deleted successfully"}
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )