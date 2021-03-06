#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join
from argparse import ArgumentParser

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


parser = ArgumentParser(description='zeromq actor test')
parser.add_argument('-r', '--role', choices=('pinger', 'ponger'),
                    required=True, help='The actor role')
parser.add_argument('-g', '--gevent', action='store_true',
                    help='Enable gevent zeromq')
args = parser.parse_args()

if args.gevent:
    import zmq.green as zmq
    from gevent import sleep
    print('gevent zeromq is enabled.')
else:
    from time import sleep
    zmq = None

if args.role == 'pinger':
    ping = Pinger('tcp://127.0.0.1:9002', 'tcp://127.0.0.1:9001', 1, zmq)
    sleep(3)
    ping.send('start')
    ping.run()
elif args.role == 'ponger':
    pong = Ponger('tcp://127.0.0.1:9001', 'tcp://127.0.0.1:9002', 1, zmq)
    pong.run()

# vim: set ts=4 sw=4 sts=4 et:
