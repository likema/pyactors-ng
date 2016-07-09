# -*- coding: utf-8 -*-
from gevent.queue import Queue
from gevent import Greenlet


class Actor(Greenlet):
    def __init__(self):
        self.inbox = Queue()
        Greenlet.__init__(self)

    def send(self, message):
        self.inbox.put(message)

    def receive(self, message):
        raise NotImplemented()

    def _run(self):
        self.running = True

        while self.running:
            message = self.inbox.get()
            self.receive(message)

# vim: ts=4 sw=4 sts=4 et:
