#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from collections import deque
pqueue = deque()

def DestroyQueue():
	while LenQueue() >0:
		pqueue.popleft()

def GetQueue():
	 item=pqueue.popleft()
	 AddQueue(item)
	 return item

def AddQueue(dict={}):
	pqueue.append(dict)

def LenQueue():
	return len(pqueue)



                