from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    country = Column(String(25), nullable=False)
    league = Column(String(25), nullable=False)
    stadium_id = Column(Integer, ForeignKey('stadium.id'), nullable=False)

    players = relationship("Player", backref="team") # One Team has many Players
