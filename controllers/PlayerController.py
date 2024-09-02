from models.player import Player
from models import db

def add_player(first_name, last_name, country, kit_number, position, age, team_id):
    new_player = Player(first_name=first_name, last_name=last_name, country=country, kit_number=kit_number, position=position, age=age, team_id=team_id)
    db.add(new_player)
    db.commit()
    return new_player

def get_players():
    players = db.query(Player).all()
    return players

def delete_player(player_id):
    player = db.query(Player).get(player_id)
    db.delete(player)
    db.commit()
    return player

def update_player(player_id, first_name, last_name, country, kit_number, position, age, team_id):
    player = db.query(Player).get(player_id)
    player.first_name = first_name
    player.last_name = last_name
    player.country = country
    player.kit_number = kit_number
    player.position = position
    player.age = age
    player.team_id = team_id
    db.commit()
    return player

def get_player(player_id):
    player = db.query(Player).get(player_id)
    return player
