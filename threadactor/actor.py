# -*- coding: utf-8 -*-
from threading import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty

from actorfactory import make_actor


Actor = make_actor(Thread, Queue, Empty)
# vim: ts=4 sw=4 sts=4 et:
