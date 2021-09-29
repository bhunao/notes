from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, unique=True)
    priority = Column(Integer, default=0)
    _deleted = Column(Boolean, default=False)
