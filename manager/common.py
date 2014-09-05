#!/usr/bin/env python
# -*- coding: utf-8 -*-

###### The below settings should be changed to reflect your environment #######

BUFSIZE=200000
PORT_BIND=3339

# this should reflect your MySQL server config:
sqlhost="127.0.0.1" 
sqluser="vmgr"
sqlpass="teste"
sqldb="vgather"

###### The below settings should kept untouched #######

GENERAL=100
BANNER=200
ARGS=300
IOFILES=400

from base64 import *
def ParseBanner(string):
	banner=""
	if len(string) > 1:
		# 8080:QXBhY2hlIFRvbWNhdC9Db3lvdGUgSlNQIGVuZ2luZQ==:2
		banner=b64decode(string.split(':')[1])
	return banner


def ParsePortCount(string):
	# 8080:QXBhY2hlIFRvbWNhdC9Db3lvdGUgSlNQIGVuZ2luZQ==:2
	pcount=0
	if len(string) > 1:
		pcount=string.split(':')[2]
	return int(pcount)

def ParseArgs(string):
	return b64decode(string)