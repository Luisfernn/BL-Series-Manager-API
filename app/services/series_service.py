from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.series import Series


def get_series_by_title(db: Session, title: str) -> Series | None:
    normalized_title = title.strip()

    return (
        db.query(Series)
        .filter(func.lower(Series.title) == func.lower(normalized_title))
        .first()
    )


def create_series(
    db: Session,
    *,
    title: str,
    status: str | None = None,
    production_company: str | None = None,
    date_start: str | None = None,
    date_watched: str | None = None,
) -> Series:
    """
    Creates a new Series if it does not already exist.
    Raises ValueError if a series with the same title already exists.
    """

    existing_series = get_series_by_title(db, title)

    if existing_series:
        raise ValueError("Series with this title already exists.")

    series = Series(
        title=title.strip(),
        status=status,
        production_company=production_company,
        date_start=date_start,
        date_watched=date_watched,
    )

    db.add(series)
    db.commit()
    db.refresh(series)

    return series
