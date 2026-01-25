from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.tag import TagCreate, TagResponse, TagUpdate
from app.services.tag_service import create_tag, get_tag_by_name, get_tag_by_id, update_tag, delete_tag

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db=db, name=tag.name)


@router.get("/by-name/{name}", response_model=TagResponse)
def get_tag_by_name_endpoint(name: str, db: Session = Depends(get_db)):
    tag = get_tag_by_name(db=db, name=name)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found"
        )

    return tag


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag_endpoint(tag_id: int, db: Session = Depends(get_db)):
    tag = get_tag_by_id(db=db, tag_id=tag_id)

    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found"
        )

    return tag


@router.put("/{tag_id}", response_model=TagResponse)
def update_tag_endpoint(
    tag_id: int,
    tag_in: TagUpdate,
    db: Session = Depends(get_db)
):
    try:
        tag = update_tag(db, tag_id, tag_in)
        return tag
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.delete("/{tag_id}")
def delete_tag_endpoint(
    tag_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_tag(db, tag_id)
        return {"message": "Tag deleted successfully"}
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )