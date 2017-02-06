# -*- coding: utf-8 -*-
from gevent.queue import Queue, Empty
from gevent import Greenlet

from actorfactory import make_actor


Actor = make_actor(Greenlet, Queue, Empty, True)
# vim: ts=4 sw=4 sts=4 et:
