from fastapi import APIRouter
from controllers import StadiumController
from pydantic import BaseModel

router = APIRouter()

class StadiumItem(BaseModel):
    name: str
    capacity: int

@router.get("/")
async def get_stadiums():
    stadiums = StadiumController.get_stadiums()
    return stadiums

@router.post("/add")
async def create_stadium(stadium: StadiumItem):
    new_stadium = StadiumController.add_stadium(stadium.name, stadium.capacity)
    return new_stadium

@router.delete("/{stadium_id}")
async def delete_stadium(stadium_id: int):
    return StadiumController.delete_stadium(stadium_id)

@router.put("/{stadium_id}")
async def update_stadium(stadium_id: int, stadium: StadiumItem):
    return StadiumController.update_stadium(stadium_id, stadium.name, stadium.capacity)
