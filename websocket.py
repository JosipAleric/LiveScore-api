from typing import Dict, Any, Set
from fastapi import WebSocket, FastAPI
from starlette.websockets import WebSocketDisconnect

TMessagePayload = Any
TActiveConnections = Dict[str, Set[WebSocket]]

connected_clients = []

# class WSManager:
#     def __init__(self):
#         self.active_connections: TActiveConnections = {}
#
#     async def connect(self, match_id: str, ws: WebSocket):
#         print(f"WebSocket connection established with match_id: {match_id}")
#         self.active_connections.setdefault(match_id, set()).add(ws)
#
#     async def disconnect(self, match_id: str, ws: WebSocket):
#         self.active_connections[match_id].remove(ws)
#
#     async def send(self, match_id: str, message: Any):
#         print(f"Sending message to match_id: {match_id}")
#         ws_set = self.active_connections.get(match_id, set())
#         for ws in ws_set:
#             print(f"Sending message to websocket: {ws}")
#             await ws.send_text(str(message))
#
# ws_manager = WSManager()


