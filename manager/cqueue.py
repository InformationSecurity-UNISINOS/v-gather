#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

class Fila(object):

        def __init__(self):
                from collections import deque
                self.pqueue = deque()

        def DestroyQueue(self):
                while self.LenQueue() >0:
                        self.pqueue.popleft()
                return True

        def GetQueue(self):
                item=self.pqueue.popleft()
                self.AddQueue(item)
                return item

        def AddQueue(self,tdict={}):
                self.pqueue.append(tdict)
                return True

        def LenQueue(self):
                return len(self.pqueue)

recvdata=Fila()
candidates=Fila()

from collections import deque
def DestroyQueue(q):
        while LenQueue(q) >0:
                q.popleft()

def GetQueue(q):
        item=q.popleft()
        AddQueue(q,item)
        return item

def AddQueue(q,tdict={}):
        q.append(tdict)

def LenQueue(q):
        return len(q)


rcv_queue= deque()
can_queue= deque()


                