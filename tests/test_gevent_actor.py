#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join
sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))

import gevent  # noqa

from geventactor import Actor  # noqa


class Pinger(Actor):
    def receive(self, message):
        print(message)
        pong.send('ping')
        gevent.sleep(1)


class Ponger(Actor):
    def receive(self, message):
        print(message)
        ping.send('pong')
        gevent.sleep(1)


ping = Pinger()
pong = Ponger()

ping.start()
pong.start()

ping.send('start')
gevent.joinall((ping, pong))
# vim: set ts=4 sw=4 sts=4 et:
