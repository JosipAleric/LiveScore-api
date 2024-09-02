from fastapi import APIRouter
from controllers import PlayerController
from pydantic import BaseModel

router = APIRouter()

class PlayerItem(BaseModel):
    first_name: str
    last_name: str
    country: str
    kit_number: int
    position: str
    age: int
    team_id: int

@router.get("/")
async def get_players():
    players = PlayerController.get_players()
    return players

@router.post("/add")
async def create_player(player: PlayerItem):
    return PlayerController.add_player(first_name=player.first_name, last_name=player.last_name, country=player.country, kit_number=player.kit_number, position=player.position, age=player.age, team_id=player.team_id)

@router.delete("/{player_id}")
async def delete_player(player_id: int):
    return PlayerController.delete_player(player_id)

@router.put("/{player_id}")
async def update_player(player_id: int, player: PlayerItem):
    return PlayerController.update_player(player_id, first_name=player.first_name, last_name=player.last_name, country=player.country, kit_number=player.kit_number, position=player.position, age=player.age, team_id=player.team_id)