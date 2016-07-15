# -*- coding: utf-8 -*-

import logging
import traceback

import zmq


class Actor(object):
    def __init__(self, sub_addr, pub_addr):
        context = zmq.Context()

        self._sub = context.socket(zmq.SUB)
        self._sub.connect(sub_addr)
        self._sub.setsockopt(zmq.SUBSCRIBE, b'')

        self._pub = context.socket(zmq.PUB)
        self._pub.bind(pub_addr)

    def send(self, message):
        self._pub.send_json(message)

    def run(self):
        while True:
            try:
                self.receive(self._sub.recv_json())
            except Exception:
                logging.error('Failed to receive message, %s',
                              traceback.format_exc())

    def receive(self, message):
        pass

# vim: ts=4 sw=4 sts=4 et:
