#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from asyncactor import Actor  # noqa


class Pinger(Actor):
    async def receive(self, message):
        print(message)
        await asyncio.sleep(3)
        pong.send('ping')

    async def handle_timeout(self):
        print('pinger timeout')


class Ponger(Actor):
    async def receive(self, message):
        print(message)
        await asyncio.sleep(3)
        ping.send('pong')

    async def handle_timeout(self):
        print('ponger timeout')


ping = Pinger(1)
pong = Ponger(1)

ping.send('start')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait((ping.run(), pong.run())))
loop.close()
# vim: ts=4 sw=4 sts=4 et:
