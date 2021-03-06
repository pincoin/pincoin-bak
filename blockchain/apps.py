from django.apps import AppConfig


class BlockchainConfig(AppConfig):
    name = 'blockchain'

    def ready(self):
        from .models import (
            WebSocket, Block
        )

        WebSocket.objects.all().delete()

        Block.objects.all().delete()
