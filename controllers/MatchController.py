from models.match import Match
# from redis_client import redis
from models import db

def add_match(home_team_id, away_team_id, match_date, attendance, stadium_id, is_match_live):
    new_match = Match(home_team_id=home_team_id, away_team_id=away_team_id, match_date=match_date, attendance=attendance, stadium_id=stadium_id, is_match_live=is_match_live)
    db.add(new_match)
    db.commit()
    return new_match

def get_matches():
    matches = db.query(Match).all()
    # home_team = matches[0].home_team.full_name
    # away_team = matches[0].away_team.full_name
    # stadium = matches[0].stadium.name
    # add home team name and away team name to response
    for match in matches:
        match.home_team_name = match.home_team.full_name
        match.away_team_name = match.away_team.full_name
        match.stadium_name = match.stadium.name
    return matches


def delete_match(match_id):
    match = db.query(Match).get(match_id)
    db.delete(match)
    db.commit()
    return match


def update_match(match_id, home_team_id, away_team_id, match_date, attendance, stadium_id, is_match_live):
    match = db.query(Match).get(match_id)
    match.home_team_id = home_team_id
    match.away_team_id = away_team_id
    match.match_date = match_date
    match.attendance = attendance
    match.stadium_id = stadium_id
    match.is_match_live = is_match_live
    db.commit()
    return match


def get_match(match_id):
    match = db.query(Match).get(match_id)
    home_team = match.home_team.full_name
    away_team = match.away_team.full_name
    stadium = match.stadium.name
    return match


def get_live_matches():
    live_matches = db.query(Match).filter(Match.is_match_live == True).all()
    response = []
    for match in live_matches:
        response.append({
            "id": match.id,
            "home_team": match.home_team.full_name,
            "away_team": match.away_team.full_name,
            "match_date": match.match_date,
            "attendance": match.attendance,
            "stadium": match.stadium.name,
            "match_results": match.match_results,
        })
    return response

def update_match_live_status(match_id):
    match = db.query(Match).get(match_id)
    match.is_match_live = not match.is_match_live
    db.commit()
    return match

