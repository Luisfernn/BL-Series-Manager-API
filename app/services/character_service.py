from sqlalchemy.orm import Session
from typing import Optional

from app.models.characters import Character
from app.models.series import Series
from app.schemas.characters import CharacterUpdate


def get_character_by_id(db: Session, character_id: int) -> Character | None:
    return db.query(Character).filter(Character.id == character_id).first()


def create_character(
    db: Session,
    *,
    name: str,
    series_id: int,
    actor_id: Optional[int] = None,
    role_type: str,
) -> Character:
    series = db.query(Series).filter(Series.id == series_id).first()
    if not series:
        raise ValueError("Series not found.")

    character = Character(
        name=name.strip(),
        series_id=series_id,
        actor_id=actor_id,
        role_type=role_type.strip(),
    )

    db.add(character)
    db.commit()
    db.refresh(character)

    return character


def update_character(db: Session, character_id: int, character_update: CharacterUpdate) -> Character:
    """Atualiza um personagem existente"""
    character = get_character_by_id(db, character_id)

    if not character:
        raise ValueError("Character not found.")

    # Atualiza apenas os campos que foram fornecidos
    update_data = character_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(character, field, value)

    db.commit()
    db.refresh(character)

    return character


def delete_character(db: Session, character_id: int) -> bool:
    """Deleta um personagem"""
    character = get_character_by_id(db, character_id)

    if not character:
        raise ValueError("Character not found.")

    db.delete(character)
    db.commit()

    return True