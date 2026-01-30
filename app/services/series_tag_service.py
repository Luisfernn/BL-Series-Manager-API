from sqlalchemy.orm import Session
from app.models.series_tag import SeriesTag
from app.services.tag_service import get_tag_by_name, create_tag
from app.services.series_service import get_series_by_title, get_series_by_id


def _add_tags_to_series_obj(db: Session, series, tag_names: list[str]) -> None:
    for name in tag_names:
        tag = get_tag_by_name(db, name)

        if not tag:
            tag = create_tag(db, name=name)

        exists = (
            db.query(SeriesTag)
            .filter(
                SeriesTag.series_id == series.id,
                SeriesTag.tag_id == tag.id,
            )
            .first()
        )

        if exists:
            continue

        association = SeriesTag(
            series_id=series.id,
            tag_id=tag.id,
        )

        db.add(association)

    db.commit()


def add_tags_to_series(
    db: Session,
    *,
    series_title: str,
    tag_names: list[str],
) -> None:
    series = get_series_by_title(db, series_title)

    if not series:
        raise ValueError(f"Series with title '{series_title}' not found. Please verify the series exists.")

    _add_tags_to_series_obj(db, series, tag_names)


def add_tags_to_series_by_id(
    db: Session,
    *,
    series_id: int,
    tag_names: list[str],
) -> None:
    series = get_series_by_id(db, series_id)

    if not series:
        raise ValueError(f"Series with id '{series_id}' not found. Please verify the series exists.")

    _add_tags_to_series_obj(db, series, tag_names)