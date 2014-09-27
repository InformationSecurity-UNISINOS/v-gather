#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from collections import deque
#def DestroyQueue(q):
#	while LenQueue(q) >0:
#		q.popleft()
#
#def GetQueue(q):
#	item=q.popleft()
#	AddQueue(q,item)
#	return item
#
#def AddQueue(q,tdict):
#	if tdict is None: tdict = {}
#	q.append(tdict)
#
#def LenQueue(q):
#	return len(q)
#rcv_queue= deque()
#can_queue= deque()

class Fila(object):
        def __init__(self):
                from collections import deque
                self.pqueue = deque()

        def DestroyQueue(self):
                while LenQueue() >0:
                        self.pqueue.popleft()
                return True

        def GetQueue(self):
                item=self.pqueue.popleft()
                self.AddQueue(item)
                return item

        def AddQueue(self,dict={}):
                self.pqueue.append(dict)
                return True

        def LenQueue(self):
                return len(self.pqueue)

recvdata=Fila()
candidates=Fila()

                