from channels.routing import route
from example.consumers import ws_connect, ws_disconnect


channel_routing = [
	route('websocket.connect', ws_connect),
	route('websocket.ws_disconnect', ws_disconnect),
]