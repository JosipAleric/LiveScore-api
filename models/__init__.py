from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.stadium import Stadium
from models.team import Team
from models.player import Player
from models.match import Match
from models.match_result import MatchResult
from models.match_event import MatchEvent
from models.user import User, TokenTable
from triggers.UpdateMatchResults import update_match_result
from triggers.CreateMatchResult import create_match_result
from procedures.CreateMatchResult import create_match_result_after_match_insert

# SQL
engine = create_engine('mysql://root:josipaleric@localhost:6306/football_matches')

# Postgres
# engine = create_engine('postgresql://postgres:josipaleric@localhost:5432/football_matches')

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
db = Session()

with engine.connect() as connection:
    connection.execute(text("DROP PROCEDURE IF EXISTS CreateMatchResultAfterMatchInsert"))
    connection.execute(text("DROP TRIGGER IF EXISTS create_match_result"))
    connection.execute(text("DROP TRIGGER IF EXISTS update_match_result"))
    connection.execute(text("DROP TRIGGER IF EXISTS after_match_insert"))

    connection.execute(text(create_match_result_after_match_insert))
    connection.execute(text(create_match_result))
    connection.execute(text(update_match_result))

