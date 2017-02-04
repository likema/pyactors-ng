#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join

import zmq.green as zmq
import gevent
from gevent import sleep

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from zmqactor import Actor  # noqa


class Pinger(Actor):
    def receive(self, message):
        print(message)
        sleep(2)
        self.send('ping')

    def handle_timeout(self):
        print('pinger timeout')


class Ponger(Actor):
    def receive(self, message):
        print(message)
        sleep(2)
        self.send('pong')

    def handle_timeout(self):
        print('ponger timeout')


def run_pinger():
    ping = Pinger('tcp://127.0.0.1:9002', 'tcp://127.0.0.1:9001', 1, zmq)
    sleep(3)
    ping.send('start')
    ping.run()


pong = Ponger('tcp://127.0.0.1:9001', 'tcp://127.0.0.1:9002', 1, zmq)
gevent.joinall((gevent.spawn(run_pinger), gevent.spawn(pong.run)))
# vim: set ts=4 sw=4 sts=4 et:
