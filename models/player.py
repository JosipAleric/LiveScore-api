from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    country = Column(String(25), nullable=False)
    kit_number = Column(Integer, nullable=False)
    position = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))

    match_events = relationship("MatchEvent", backref="player")  # One Player can have many Match Events
    # associated_team = relationship("Team")  # One Player belongs to one Team
