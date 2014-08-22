#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from common import *


def SerializeData(data):
    import pickle
    import pickletools
    
    return pickle.dumps(data)

def SendData():
    from multiprocessing.connection import Client
    client = Client((MANAGER, PORTA))
    serialized = SerializeData(nlist)
    print "size of stream: %d" %(len(serialized))
    client.send(serialized)


def SendData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        try:
            sock.connect((MANAGERADDR, PORTA))
        except:
            print "Impossível conectar no Manager"
            sys.exit(3)
    
        sock.sendall(serialized)
        
    finally:
        sock.close()
