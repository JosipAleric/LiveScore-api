from fastapi import APIRouter
from controllers import TeamController
from pydantic import BaseModel

router = APIRouter()

class TeamItem(BaseModel):
    full_name: str
    stadium_id: int
    country: str
    league: str

@router.get("/")
async def get_teams():
    teams = TeamController.get_teams()
    return teams

@router.post("/add")
async def create_team(team: TeamItem):
    return TeamController.add_team(full_name=team.full_name, stadium_id=team.stadium_id, country=team.country, league=team.league)

@router.delete("/{team_id}")
async def delete_team(team_id: int):
    return TeamController.delete_team(team_id)

@router.put("/{team_id}")
async def update_team(team_id: int, team: TeamItem):
    return TeamController.update_team(team_id, full_name=team.full_name, stadium_id=team.stadium_id, country=team.country, league=team.league)

@router.get("/{team_id}")
async def get_team(team_id: int):
    return TeamController.get_team(team_id)