# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue

try:
    from Queue import Empty
except ImportError:
    from queue import Empty

from actorfactory import make_actor


Actor = make_actor(Process, Queue, Empty)
# vim: ts=4 sw=4 sts=4 et:
