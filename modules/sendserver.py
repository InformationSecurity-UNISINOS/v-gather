#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from common import *


def SerializeData(data):
    import pickle
    import pickletools
    return pickle.dumps(data)

#def SendData():
#    from multiprocessing.connection import Client
#    client = Client((MANAGERADDR, PORTA))
#    serialized = SerializeData(nlist)
#    print "size of stream: %d" %(len(serialized))
#    client.send(serialized)
#    client.close()

def SendData(string):
    import xmlrpclib
    remote_server="http://"+MANAGER+":"+PORTA
    s = xmlrpclib.Server(remote_server)
    s.echo(string)