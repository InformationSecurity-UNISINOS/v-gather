#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Fila(object):

    def __init__(self):
        from collections import deque
        self.pqueue = deque()

    def DestroyQueue(self):
        while self.LenQueue() > 0:
            self.pqueue.popleft()
        return True

    def GetQueue(self):
        item = self.pqueue.popleft()
        self.AddQueue(item)
        return item

    def AddQueue(self, dict={}):
        self.pqueue.append(dict)
        return True

    def LenQueue(self):
        return len(self.pqueue)

recvdata = Fila()
candidates = Fila()
filtro = Fila()
