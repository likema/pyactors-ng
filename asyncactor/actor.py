# -*- coding: utf-8 -*-
import asyncio


class Actor(object):
    def __init__(self):
        self.inbox = asyncio.Queue()

    def send(self, message):
        self.inbox.put_nowait(message)

    async def receive(self, message):
        raise NotImplemented()

    async def run(self):
        self.running = True

        while self.running:
            message = await self.inbox.get()
            await self.receive(message)

# vim: ts=4 sw=4 sts=4 et:
