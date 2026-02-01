from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.characters import Character
from app.models.series import Series
from app.services.actor_service import get_actor_by_nickname


def get_character_by_id(db: Session, character_id: int) -> Character | None:
    return db.query(Character).filter(Character.id == character_id).first()


def get_character_by_name_in_series(db: Session, name: str, series_id: int) -> Character | None:
    """
    Busca personagem por nome dentro de uma série específica (case-insensitive).
    Normaliza apenas para comparação, não altera o valor salvo.
    """
    normalized = name.strip()
    return (
        db.query(Character)
        .filter(
            func.lower(Character.name) == func.lower(normalized),
            Character.series_id == series_id
        )
        .first()
    )


def create_character(
    db: Session,
    *,
    name: str,
    series_id: int,
    actor_nickname: str,
    role_type: str,
) -> Character:
    series = db.query(Series).filter(Series.id == series_id).first()
    if not series:
        raise ValueError(f"Series with id {series_id} not found. Please verify the series exists.")

    actor = get_actor_by_nickname(db, actor_nickname)
    if not actor:
        raise ValueError(f"Ator com nickname '{actor_nickname}' não encontrado. Verifique se o ator já foi cadastrado.")

    character = Character(
        name=name.strip(),
        series_id=series_id,
        actor_id=actor.id,
        role_type=role_type.strip(),
    )

    db.add(character)
    db.commit()
    db.refresh(character)

    return character