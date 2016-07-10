# -*- coding: utf-8 -*-
from message import observable

from .actor import Actor


@observable
class Publisher(Actor):
    def __init__(self, subject, receive_timeout=None):
        self.subject = subject
        Actor.__init__(self, receive_timeout)

    def subcribe(self, observer):
        self.sub(self.subject, observer.send)

    def publish(self, message):
        self.pub(self.subject, message)

# vim: ts=4 sw=4 sts=4 et:
