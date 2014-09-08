#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import *
def ParseBanner(string,pos):
	import re
	banner=""
	if len(string) > 1:
		lista=[]
		size=len(string.split(':'))-1
		for i in xrange(0,size,2):
			tok1=string.split(':')[i]       				# port
			tok2=string.split(':')[i+1]     				# banner/finger print
			if not tok2.isspace() and tok2 is not "":		# if we got a banner and not a space or tabs, or any trash values
				banner=b64decode(tok2)  					# so decode it
			else:
				banner=tok2                  				# or, just use it as is (empty)

			buf=tok1+":"+banner
			lista.append(buf)

			print "DEBUG->ParseBanner: %s" %str(lista[pos])
		try:
			return len(lista),lista[pos]
		except:
			return len(lista),False


def ParsePortCount(string):
	# 8080:QXBhY2hlIFRvbWNhdC9Db3lvdGUgSlNQIGVuZ2luZQ==:8005::8009:QXBhY2hlIEpzZXJ2:"
	pcount=0
	if len(string) > 1:
		pcount=string.split(':')[2]
	return int(pcount)

def ParseArgs(string):
	return b64decode(string)
