# mmd/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumer import AuctionConsumer

websocket_urlpatterns = [
    path('ws/auction/<int:emlak_id>/', AuctionConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
    # HTTP istekleri için DRF'yi kullanabilirsiniz
})
