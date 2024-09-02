from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base

class Stadium(Base):
    __tablename__ = 'stadium'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    capacity = Column(Integer, nullable=False)

    teams = relationship("Team", backref="stadium")  # One Stadium can have many Teams
    matches = relationship("Match", backref="stadium")  # One Stadium can have many Matches
