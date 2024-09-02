import asyncio

from fastapi import FastAPI
from app.routers import match_events, stadiums, teams, players, matches, users
from fastapi.middleware.cors import CORSMiddleware
from fastapi import (
    FastAPI, WebSocket, WebSocketDisconnect,
    status, Depends, Request, Response
)
from websocket import connected_clients

app = FastAPI()
# disable cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# async def send_event_to_clients(event: str):
#     for client in connected_clients:
#         await client.send_text(event)
#

@app.websocket("/match_events")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle received data if needed
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         await websocket.send_text("Hello, client!")
#     except WebSocketDisconnect:
#         print("WebSocket disconnected")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


app.include_router(match_events.router, prefix="/match_events", tags=["Match Events"])
app.include_router(stadiums.router, prefix="/stadiums", tags=["Stadiums"])
app.include_router(teams.router, prefix="/teams", tags=["Teams"])
app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(matches.router, prefix="/matches", tags=["Matches"])
app.include_router(users.router, prefix="/users", tags=["Users"])

