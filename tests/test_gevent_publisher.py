#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join

import gevent

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from geventactor import Publisher  # noqa


class Pinger(Publisher):
    def receive(self, message):
        print(message)
        gevent.sleep(2)
        self.publish('ping')

    def handle_timeout(self):
        print('pinger timeout')


class Ponger(Publisher):
    def receive(self, message):
        print(message)
        gevent.sleep(2)
        self.publish('ping')

    def handle_timeout(self):
        print('ponger timeout')


ping = Pinger('evt.ping', 1)
pong = Ponger('evt.pong', 1)

ping.subcribe(pong)
pong.subcribe(ping)
ping.start()
pong.start()

ping.publish('start')
gevent.joinall([ping, pong])
# vim: set ts=4 sw=4 sts=4 et:
