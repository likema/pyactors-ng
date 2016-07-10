#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join

import asyncio

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from asyncactor import Publisher  # noqa


class Pinger(Publisher):
    async def receive(self, message):
        print(message)
        await asyncio.sleep(3)
        self.publish('ping')

    async def handle_timeout(self):
        print('Pinger timeout')


class Ponger(Publisher):
    async def receive(self, message):
        print(message)
        await asyncio.sleep(3)
        self.publish('pong')

    async def handle_timeout(self):
        print('Ponger timeout')


ping = Pinger('evt.ping', 1)
pong = Ponger('evt.pong', 1)

ping.subcribe(pong)
pong.subcribe(ping)
ping.publish('start')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait((ping.run(), pong.run())))
loop.close()
# vim: ts=4 sw=4 sts=4 et:
