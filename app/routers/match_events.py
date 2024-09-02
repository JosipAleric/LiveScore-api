from fastapi import APIRouter
from controllers import MatchEventController
from pydantic import BaseModel

router = APIRouter()

class MatchEvent(BaseModel):
    event_description: str
    player_id: int
    match_id: int
    minute: int

@router.get("/{match_id}")
async def get_match_events(match_id: int):
    events = MatchEventController.get_match_events(match_id)
    return events

@router.post("/add")
async def create_match_event(match_event: MatchEvent):
    match_event = await MatchEventController.add_match_event(match_id=match_event.match_id, player_id=match_event.player_id, event_description=match_event.event_description, minute=match_event.minute)
    return match_event

@router.delete("/{match_event_id}")
async def delete_match_event(match_event_id: int):
    match_event = MatchEventController.delete_match_event(match_event_id)
    return match_event

@router.put("/{match_event_id}")
async def update_match_event(match_event_id: int, match_event: MatchEvent):
    match_event = MatchEventController.update_match_event(match_event_id, match_event)
    return match_event