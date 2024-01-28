import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from mmd.consumer import AuctionConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmd.settings')

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    # Her emlak için dinamik bir WebSocket yolu
    path('ws/auction/<int:emlak_id>/', AuctionConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
