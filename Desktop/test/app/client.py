from channels.consumer import AsyncConsumer

import json
import scrape
from app import models, serializers
from asgiref.sync import sync_to_async
from pprint import pprint

# @sync_to_async
# def _get_data():
#     games = models.Game.objects.all()
#     serializer = serializers.GameSerializer(games, many=True)
#     return serializer.data
#
#
# @sync_to_async
# def _get_datas():
#     game = models.Game.objects.all()
#     return game


class PracticeConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("retrive", event, type(event))

        if event["text"] == "1":
            data = scrape.scrape_data()
            pprint(data)
            await self.send({"type": "websocket.send", "text": json.dumps(data)})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
