#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base64 import *
from common import *

def ParseBanner(string,pos):
	
	banner=""
	if len(string) > 1:
		lista=[]
		size=len(string.split(':'))-1
		for i in xrange(0,size,2):
			banner=string.split(':')[i]+":"+string.split(':')[i+1]
			lista.append(banner)
		try:
			return len(lista),lista[pos]
		except:
			return len(lista),False

def CheckKnownTcpPort(string):
	port=string.split(':')[0]
	if any(port in s for s in tcp_ports_already_verirified):
		return True	# ja foi verificado
	else:
		tcp_ports_already_verirified.append(port)
		return False # ainda nao foi verificado

def CheckKnownUdpPort(string):
	port=string.split(':')[0]
	if any(port in s for s in udp_ports_already_verirified):
		return True	# ja foi verificado
	else:
		udp_ports_already_verirified.append(port)
		return False  # ainda nao foi verificado


def ParsePortCount(string):
	# 8080:QXBhY2hlIFRvbWNhdC9Db3lvdGUgSlNQIGVuZ2luZQ==:8005::8009:QXBhY2hlIEpzZXJ2:"
	pcount=0
	if len(string) > 1:
		pcount=string.split(':')[2]
	return int(pcount)

def ParseArgs(string):
	return b64decode(string)
