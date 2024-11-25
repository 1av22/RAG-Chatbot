from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from ..utils.database import Base
from .userModel import User


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    link = Column(String, nullable=False)

    # Relationship to the 'users' table
    user = relationship("User", back_populates="files")
