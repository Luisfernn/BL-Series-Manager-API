from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.tags import Tag
from app.schemas.tag import TagUpdate


def get_tag_by_name(db: Session, name: str) -> Tag | None:
    normalized_name = name.strip()

    return (
        db.query(Tag)
        .filter(func.lower(Tag.name) == func.lower(normalized_name))
        .first()
    )


def get_tag_by_id(db: Session, tag_id: int) -> Tag | None:
    return db.query(Tag).filter(Tag.id == tag_id).first()


def create_tag(db: Session, *, name: str) -> Tag:
    """
    Creates a tag if it does not exist.
    Returns the existing tag otherwise.
    """

    existing_tag = get_tag_by_name(db, name)
    if existing_tag:
        return existing_tag

    tag = Tag(name=name.strip())
    db.add(tag)
    db.commit()
    db.refresh(tag)

    return tag


def update_tag(db: Session, tag_id: int, tag_update: TagUpdate) -> Tag:
    """Atualiza uma tag existente"""
    tag = get_tag_by_id(db, tag_id)

    if not tag:
        raise ValueError("Tag not found.")

    # Atualiza apenas os campos que foram fornecidos
    update_data = tag_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(tag, field, value)

    db.commit()
    db.refresh(tag)

    return tag


def delete_tag(db: Session, tag_id: int) -> bool:
    """Deleta uma tag"""
    tag = get_tag_by_id(db, tag_id)

    if not tag:
        raise ValueError("Tag not found.")

    db.delete(tag)
    db.commit()

    return True