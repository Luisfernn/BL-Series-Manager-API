from sqlalchemy.orm import Session
from app.models.series import Series


def get_series_by_title(db: Session, title: str) -> Series | None:
    """
    Busca uma série pelo título exato.
    Retorna a série se existir, ou None se não existir.
    """
    return db.query(Series).filter(Series.title == title).first()
