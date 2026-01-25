from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class SeriesTag(Base):
    __tablename__ = "series_tag"

    series_id = Column(ForeignKey("series.id"), Integer, nullable=False, unique=True)
    tag_id = Column(ForeignKey("tags.id"), Integer, nullable=False, unique=True)
