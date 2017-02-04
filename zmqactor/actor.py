# -*- coding: utf-8 -*-

import logging
import traceback

import zmq


class Actor(object):
    def __init__(self, sub_addr, pub_addr, receive_timeout=None):
        context = zmq.Context()

        self._sub = context.socket(zmq.SUB)
        self._sub.connect(sub_addr)
        self._sub.setsockopt(zmq.SUBSCRIBE, b'')

        self._pub = context.socket(zmq.PUB)
        self._pub.bind(pub_addr)
        self.receive_timeout = receive_timeout * 1000

    def send(self, message):
        self._pub.send_json(message)

    def receive(self, message):
        pass

    def handle_timeout(self):
        pass

    def run(self):
        while True:
            try:
                events = self._sub.poll(timeout=self.receive_timeout)
                if events:
                    for i in xrange(events):
                        self.receive(self._sub.recv_json())
                else:
                    self.handle_timeout()
            except Exception:
                logging.error('Failed to receive message, %s',
                              traceback.format_exc())

# vim: ts=4 sw=4 sts=4 et: