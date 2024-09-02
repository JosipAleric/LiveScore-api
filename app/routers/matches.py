from fastapi import APIRouter
from controllers import MatchController
from pydantic import BaseModel

router = APIRouter()

class MatchItem(BaseModel):
    home_team_id: int
    away_team_id: int
    stadium_id: int
    date: str
    attendance: int
    is_match_live: bool

@router.get("/")
async def get_matches():
    matches = MatchController.get_matches()
    return matches


@router.post("/add")
async def create_match(match: MatchItem):
    return MatchController.add_match(home_team_id=match.home_team_id, away_team_id=match.away_team_id, match_date=match.date, attendance=match.attendance, stadium_id=match.stadium_id, is_match_live=False)


@router.delete("/{match_id}")
async def delete_match(match_id: int):
    return MatchController.delete_match(match_id)


@router.put("/{match_id}")
async def update_match(match_id: int, match: MatchItem):
    return MatchController.update_match(match_id, home_team_id=match.home_team_id, away_team_id=match.away_team_id, match_date=match.date, attendance=match.attendance, stadium_id=match.stadium_id, is_match_live=match.is_match_live)


@router.get("/details/{match_id}")
async def get_match(match_id: int):
    return MatchController.get_match(match_id)


@router.get("/live_matches")
async def live_matches():
    return MatchController.get_live_matches()

@router.post("/update_match_live_status/{match_id}")
async def update_match_live_status(match_id: int):
    return MatchController.update_match_live_status(match_id)


