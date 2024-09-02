from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from models import Base

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_date = Column(String(25), nullable=False)
    attendance = Column(Integer)
    stadium_id = Column(Integer, ForeignKey('stadium.id'))
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    is_match_live = Column(Boolean, default=False)

    match_results = relationship("MatchResult", backref="match")  # One Match has one MatchResult
    match_events = relationship("MatchEvent", backref="match")  # One Match has many Match Events

    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    # associated_stadium = relationship("Stadium")  # One Match belongs to one Stadium




