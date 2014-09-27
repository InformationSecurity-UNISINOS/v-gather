#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
def DestroyQueue(q):
        while LenQueue(q) >0:
                q.popleft()

def GetQueue(q):
        item=q.popleft()
        AddQueue(q,item)
        return item

def AddQueue(q,tdict=None):
		if tdict is None: tdict = {}
        q.append(tdict)

def LenQueue(q):
        return len(q)


rcv_queue= deque()
can_queue= deque()


                