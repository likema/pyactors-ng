# -*- coding: utf-8 -*-
import asyncio


class Actor(object):
    def __init__(self, receive_timeout=None):
        self.inbox = asyncio.Queue()
        self.receive_timeout = receive_timeout

    def send(self, message):
        self.inbox.put_nowait(message)

    async def receive(self, message):
        raise NotImplemented()

    async def handle_timeout(self):
        pass

    async def run(self):
        self.running = True

        while self.running:
            try:
                message = await asyncio.wait_for(self.inbox.get(),
                                                 self.receive_timeout)
            except asyncio.TimeoutError:
                await self.handle_timeout()
            else:
                await self.receive(message)

# vim: ts=4 sw=4 sts=4 et:
