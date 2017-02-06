# -*- coding: utf-8 -*-
from message import observable


def make_publisher(actor):
    @observable
    class Publisher(actor):
        def __init__(self, subject, receive_timeout=None):
            self.subject = subject
            actor.__init__(self, receive_timeout)

        def subcribe(self, observer):
            self.sub(self.subject, observer.send)

        def publish(self, message):
            self.pub(self.subject, message)

    return Publisher


def make_actor(base, queue, empty, underscore_run=False):
    def run(self):
        self.running = True

        while self.running:
            try:
                message = self.inbox.get(True, self.receive_timeout)
            except empty:
                self.handle_timeout()
            else:
                self.receive(message)

    class Actor(base):
        def __init__(self, receive_timeout=None):
            self.inbox = queue()
            self.receive_timeout = receive_timeout
            base.__init__(self)

        def send(self, message):
            self.inbox.put_nowait(message)

        def receive(self, message):
            raise NotImplemented()

        def handle_timeout(self):
            pass

    setattr(Actor, '_run' if underscore_run else 'run', run)
    return Actor

# vim: ts=4 sw=4 sts=4 et:
