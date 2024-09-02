from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models import Base

class MatchResult(Base):
    __tablename__ = 'match_results'

    # Match_id as primary key and foreign key referencing Matches.id (one-to-one)
    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    winner = Column(String(10))
    home_team_goals = Column(Integer, nullable=False)
    away_team_goals = Column(Integer, nullable=False)

    # associated_match = relationship("Match")  # One MatchResult belongs to one Match