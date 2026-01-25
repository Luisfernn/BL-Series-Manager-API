from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class SeriesTag(Base):
    __tablename__ = "series_tag"

    series_id = Column(Integer, ForeignKey("series.id"), nullable=False, primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False, primary_key=True)
