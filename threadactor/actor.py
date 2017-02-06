# -*- coding: utf-8 -*-
from threading import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty


class Actor(Thread):
    def __init__(self, receive_timeout=None):
        Thread.__init__(self)
        self.inbox = Queue()
        self.receive_timeout = receive_timeout

    def send(self, message):
        self.inbox.put_nowait(message)

    def receive(self, message):
        raise NotImplemented()

    def handle_timeout(self):
        pass

    def run(self):
        self.running = True
        while self.running:
            try:
                message = self.inbox.get(True, self.receive_timeout)
            except Empty:
                self.handle_timeout()
            else:
                self.receive(message)

# vim: ts=4 sw=4 sts=4 et:
