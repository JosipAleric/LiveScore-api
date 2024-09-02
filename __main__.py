import json

from models import db
from models.stadium import Stadium
from models.team import Team
from models.player import Player
from models.match import Match
from models.match_result import MatchResult
from models.match_event import MatchEvent
from redis_client import redis
from controllers import MatchEventController
from controllers import StadiumController

# anfield = Stadium(name='Anfield', capacity=63000)
# etihad = Stadium(name='Etihad', capacity=59000)
# db.add_all([anfield, etihad])
# db.commit()
# #
# liverpool = Team(full_name='Liverpool', country='England', league='Premier League', stadium=anfield)
# manchester_city = Team(full_name='Manchester City', country='England', league='Premier League', stadium=etihad)
# db.add_all([liverpool, manchester_city])
# db.commit()
# #
# salah = Player(first_name='Mohamed', last_name='Salah', country='Egypt', kit_number=11, position='RW', age=28, team = liverpool)
# van_dijk = Player(first_name='Virgil', last_name='van Dijk', country='Netherlands', kit_number=4, position='CB', age=29, team = liverpool)
# de_bruyne = Player(first_name='Kevin', last_name='de Bruyne', country='Belgium', kit_number=17, position='CM', age=29, team = manchester_city)
# haaland = Player(first_name='Erling', last_name='Haaland', country='Norway', kit_number=9, position='ST', age=20, team = manchester_city)
# db.add_all([salah, van_dijk, de_bruyne, haaland])
# db.commit()
# #
# match1 = Match(match_date='20.04.2024', attendance=50000, stadium=anfield, home_team=liverpool, away_team=manchester_city)
# db.add(match1)
# db.commit()
#
# match_result1 = MatchResult(match=match1, home_team_goals=2, away_team_goals=1)
# db.add(match_result1)
# db.commit()
# #
# match_event1 = MatchEvent(match=match1, player=salah, event_description='Goal', minute=45)
# match_event2 = MatchEvent(match=match1, player=salah, event_description='Goal', minute=50)
# match_event3 = MatchEvent(match=match1, player=de_bruyne, event_description='Yellow Card', minute=60)
# match_event4 = MatchEvent(match=match1, player=haaland, event_description='Goal', minute=90)
# db.add_all([match_event1, match_event2, match_event3, match_event4])
# db.commit()

# match2 = Match(match_date='25.07.2024', attendance=65000, stadium_id=18, home_team_id=18, away_team_id=17)
# db.add(match2)
# db.commit()

# match_event4 = MatchEvent(match_id=12, player_id=31, event_description='Goal', minute=91)
# db.add(match_event4)
# db.commit()

# events = MatchEventController.get_match_events(9)
# for event in events:
#     print(event['event_description'], event['player_name'], event['match_date'], event['home_team'], event['away_team'], event['home_team_goals'], event['away_team_goals'])

# MatchEventController.add_match_event(9, 29, 'Goal', 45)
# for event in db.query(MatchEvent).all():
#     print(event.event_description, event.player.first_name, event.player.last_name, event.match.match_date, event.match.home_team.full_name, event.match.away_team.full_name, event.match.match_results[0].home_team_goals, event.match.match_results[0].away_team_goals)