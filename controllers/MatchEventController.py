from models.match_event import MatchEvent
from models.match import Match
from models.match_result import MatchResult
import json
# from redis_client import redis
from models import db
import time
# from confluent_kafka import KafkaException
# from kafka.consumer import consumer, recieve_message
# from kafka.producer import producer, delivery_report
from websocket import connected_clients
from fastapi import WebSocket

message_delivered = False

class MatchEventEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MatchEvent):
            return {
                'id': obj.id,
                'event_description': obj.event_description,
                'player_name': f"{obj.player.first_name} {obj.player.last_name}",
                'match_date': obj.match.match_date,
                'home_team': obj.match.home_team.full_name,
                'away_team': obj.match.away_team.full_name,
                'home_team_goals': obj.match.match_results[0].home_team_goals,
                'away_team_goals': obj.match.match_results[0].away_team_goals,
                'minute': obj.minute
            }
        return super().default(obj)

def get_match_events(match_id):
    cache_key = f"match_events: {match_id}"
    # events = redis.get(cache_key)
    start_time = time.time()  # Record start time

    # if events:
    #     end_time = time.time()  # Record end time
    #     print('Cache hit')
    #     print(f'Vrijeme izvodjenja: {end_time - start_time} seconds')
    #     events = json.loads(events)
    #     return events

    print('Cache miss')
    events = db.query(MatchEvent).filter_by(match_id=match_id).all()
    events_json = json.dumps(events, cls=MatchEventEncoder)  # Use custom encoder
    # redis.set(cache_key, events_json)
    # redis.expire(cache_key, 500)

    end_time = time.time()  # Record end time
    print(f'Vrijeme izvodjenja: {end_time - start_time} seconds')

    serialized_events = json.loads(events_json)
    return serialized_events

async def add_match_event(match_id, player_id, event_description, minute):
    # Add the match event to the database
    match_event = MatchEvent(match_id=match_id, player_id=player_id, event_description=event_description, minute=minute)
    db.add(match_event)
    db.commit()

    # Get the player, home team, and away team names
    player = match_event.player.first_name + ' ' + match_event.player.last_name
    home_team = match_event.match.home_team.full_name
    away_team = match_event.match.away_team.full_name

    # Create a message for the Kafka topic
    event = f'Događaj: {event_description} za igrača {player} u minuti {minute} za utakmicu između {home_team} i {away_team}'

    if event_description == 'Goal':
        print('Sending event to clients')
        goals = {
            'home_team_goals': match_event.match.match_results[0].home_team_goals,
            'away_team_goals': match_event.match.match_results[0].away_team_goals
        }
        response = {
            'event': event,
            'match_id': match_id,
            'goals': goals
        }
        for client in connected_clients:
            print(client)
            await client.send_text(str(response))
    else:
        print('Sending event to clients')
        response = {
            'event': event,
            'match_id': match_id
        }
        for client in connected_clients:
            print(client)
            await client.send_text(str(response))

    # try:
    #     # Produce a message to the Kafka topic
    #     producer.produce('match_events', event, callback=delivery_report)
    #     producer.flush()
    #
    # except KafkaException as e:
    #     print(f'Failed to send message: {e}')


    # return encoded match event
    formatted_match_event = json.loads(json.dumps(match_event, cls=MatchEventEncoder))
    return formatted_match_event

def delete_match_event(match_event_id):
    # Delete the match event from the database
    match_event = db.query(MatchEvent).filter_by(id=match_event_id).first()

    # update goals in match results table when goal is deleted
    match_results = db.query(MatchResult).filter_by(match_id=match_event.match_id).first()
    if match_event.event_description == 'Goal':
        if match_event.player.team_id == match_event.match.home_team_id:
            match_results.home_team_goals -= 1
        else:
            match_results.away_team_goals -= 1
    db.delete(match_event)
    db.commit()
    return match_event

def update_match_event(match_event_id, match_event):
    # Update the match event in the database
    old_match_event = db.query(MatchEvent).filter_by(id=match_event_id).first()
    old_match_event.event_description = match_event.event_description
    old_match_event.minute = match_event.minute
    old_match_event.player_id = match_event.player_id
    db.commit()

    # return encoded match event
    formatted_match_event = json.loads(json.dumps(old_match_event, cls=MatchEventEncoder))
    return formatted_match_event


