#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from threadactor import Actor  # noqa


class Pinger(Actor):
    def receive(self, message):
        print(message)
        time.sleep(2)
        pong.send('ping')

    def handle_timeout(self):
        print('pinger timeout')


class Ponger(Actor):
    def receive(self, message):
        print(message)
        time.sleep(2)
        ping.send('pong')

    def handle_timeout(self):
        print('ponger timeout')


ping = Pinger(1)
pong = Ponger(1)

ping.start()
pong.start()

ping.send('start')

pong.join()
ping.join()
# vim: set ts=4 sw=4 sts=4 et:
