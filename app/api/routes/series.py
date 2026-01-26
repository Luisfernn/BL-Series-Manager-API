from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from fastapi import Query
from typing import List
from app.schemas.series import SeriesCreate, SeriesResponse, SeriesDetailResponse
from app.services.series_service import create_series, list_series, get_series_by_id, get_series_with_details
from app.services.series_tag_service import add_tags_to_series
from app.schemas.series_tags import SeriesTagsAdd
from app.schemas.series_actors import SeriesActorsAdd
from app.services.series_actor_service import add_actors_to_series
from app.schemas.series_characters import SeriesCharactersAdd
from app.services.series_character_service import add_characters_to_series
from app.schemas.ship_actors_series import ShipActorsSeriesCreate
from app.services.ship_actors_series_service import add_ship_actor_to_series


router = APIRouter(prefix="/series", tags=["Series"])


@router.post(
    "",
    response_model=SeriesResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_series_endpoint(
    series_in: SeriesCreate,
    db: Session = Depends(get_db),
):
    try:
        series = create_series(db, series_in)
        return series

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.post("/{title}/tags", status_code=status.HTTP_200_OK)
def add_tags_to_series_endpoint(
    title: str,
    payload: SeriesTagsAdd,
    db: Session = Depends(get_db),
):
    try:
        add_tags_to_series(
            db,
            series_title=title,
            tag_names=payload.tags,
        )
        return {"message": "Tags adicionadas com sucesso."}
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.post(
    "/{series_id}/actors",
    status_code=status.HTTP_200_OK,
)
def add_actors_to_series_endpoint(
    series_id: int,
    payload: SeriesActorsAdd,
    db: Session = Depends(get_db),
):
    try:
        add_actors_to_series(
            db,
            series_id=series_id,
            actor_ids=payload.actor_ids,
        )
        return {"message": "Atores adicionados com sucesso."}

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) 


@router.post(
    "/{series_id}/characters",
    status_code=status.HTTP_200_OK,
)
def add_characters_to_series_endpoint(
    series_id: int,
    payload: SeriesCharactersAdd,
    db: Session = Depends(get_db),
):
    try:
        add_characters_to_series(
            db,
            series_id=series_id,
            character_ids=payload.character_ids,
        )
        return {"message": "Personagens adicionados com sucesso."}

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )               


@router.get(
    "",
    response_model=List[SeriesResponse],
    status_code=status.HTTP_200_OK,
)
def list_series_endpoint(
    search: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return list_series(db, search=search)


@router.get(
    "/{series_id}",
    response_model=SeriesDetailResponse,
    status_code=status.HTTP_200_OK,
)
def get_series_endpoint(
    series_id: int,
    db: Session = Depends(get_db),
):
    series = get_series_with_details(db, series_id)
    if not series:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Series not found"
        )
    return series


@router.post(
    "/{series_id}/ship-actors",
    status_code=status.HTTP_200_OK,
)
def add_ship_actors_to_series_endpoint(
    series_id: int,
    payload: ShipActorsSeriesCreate,
    db: Session = Depends(get_db),
):
    try:
        add_ship_actor_to_series(
            db,
            series_id=series_id,
            ship_actor_id=payload.ship_id,
        )
        return {"message": "Ship de atores associado à série com sucesso."}

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )