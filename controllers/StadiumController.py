from models.stadium import Stadium
from models import db

def get_stadiums():
    stadiums = db.query(Stadium).all()
    return stadiums

def add_stadium(name, capacity):
    new_stadium = Stadium(name=name, capacity=capacity)
    db.add(new_stadium)
    db.commit()
    return new_stadium

def delete_stadium(stadium_id):
    stadium = db.query(Stadium).get(stadium_id)
    db.delete(stadium)
    db.commit()
    return stadium

def update_stadium(stadium_id, name, capacity):
    stadium = db.query(Stadium).get(stadium_id)
    stadium.name = name
    stadium.capacity = capacity
    db.commit()
    return stadium