from models.team import Team
from models import db

def add_team(full_name, country, league, stadium_id):
    new_team = Team(full_name=full_name, country=country, league=league, stadium_id=stadium_id)
    db.add(new_team)
    db.commit()
    return new_team

def get_teams():
    teams = db.query(Team).all()
    return teams

def delete_team(team_id):
    team = db.query(Team).get(team_id)
    db.delete(team)
    db.commit()
    return team

def update_team(team_id, full_name, country, league, stadium_id):
    team = db.query(Team).get(team_id)
    team.full_name = full_name
    team.country = country
    team.league = league
    team.stadium_id = stadium_id
    db.commit()
    return team

def get_team(team_id):
    team = db.query(Team).get(team_id)
    return team