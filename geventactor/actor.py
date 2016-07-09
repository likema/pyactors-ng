# -*- coding: utf-8 -*-
from gevent.queue import Queue, Empty
from gevent import Greenlet


class Actor(Greenlet):
    def __init__(self, receive_timeout=None):
        self.inbox = Queue()
        self.receive_timeout = receive_timeout
        Greenlet.__init__(self)

    def send(self, message):
        self.inbox.put(message)

    def receive(self, message):
        raise NotImplemented()

    def handle_timeout(self):
        pass

    def _run(self):
        self.running = True

        while self.running:
            try:
                message = self.inbox.get(True, self.receive_timeout)
            except Empty:
                self.handle_timeout()
            else:
                self.receive(message)

# vim: ts=4 sw=4 sts=4 et:
