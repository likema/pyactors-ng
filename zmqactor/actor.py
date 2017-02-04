# -*- coding: utf-8 -*-

import logging
import traceback
from sys import version_info


# xrange no longer exits since python 3.0
if version_info >= (3, 0):
    xrange = range


class Actor(object):
    def __init__(
            self, sub_addr, pub_addr=None, receive_timeout=None, zmq=None):
        if not zmq:
            import zmq

        context = zmq.Context()

        self._sub = context.socket(zmq.SUB)
        self._sub.connect(sub_addr)
        self._sub.setsockopt(zmq.SUBSCRIBE, b'')

        if pub_addr:
            self._pub = context.socket(zmq.PUB)
            self._pub.bind(pub_addr)
        else:
            self._pub = None

        self.receive_timeout = receive_timeout * 1000

    def send(self, message):
        if self._pub:
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
