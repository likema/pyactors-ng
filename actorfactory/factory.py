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

# vim: ts=4 sw=4 sts=4 et:
