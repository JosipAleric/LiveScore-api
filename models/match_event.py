
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class MatchEvent(Base):
    __tablename__ = 'match_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    minute = Column(Integer, nullable=False)
    event_description = Column(String(50), nullable=False)
    match_id = Column(Integer, ForeignKey('matches.id'))
    player_id = Column(Integer, ForeignKey('players.id'))

    # associated_match = relationship("Match")  # Event belongs to one Match (Foreign Key)
    # associated_match = relationship("Player")  # Event can involve one Player (Foreign Key)