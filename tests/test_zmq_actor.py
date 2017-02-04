#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(sys.argv[0]), '..')))
from zmqactor import Actor  # noqa


class Pinger(Actor):
    def receive(self, message):
        print(message)
        time.sleep(2)
        self.send('ping')

    def handle_timeout(self):
        print('pinger timeout')


class Ponger(Actor):
    def receive(self, message):
        print(message)
        time.sleep(2)
        self.send('pong')

    def handle_timeout(self):
        print('ponger timeout')


if len(sys.argv) == 2:
    if sys.argv[1] == 'pinger':
        ping = Pinger('tcp://127.0.0.1:9002', 'tcp://127.0.0.1:9001', 1)
        time.sleep(3)
        ping.send('start')
        ping.run()
    elif sys.argv[1] == 'ponger':
        pong = Ponger('tcp://127.0.0.1:9001', 'tcp://127.0.0.1:9002', 1)
        pong.run()

# vim: set ts=4 sw=4 sts=4 et:
