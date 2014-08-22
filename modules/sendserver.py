#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from common import *


def SerializeData(data):
    import pickle
    import pickletools
    import base64
    
    return base64.b64encode(pickle.dumps(data))

def SendData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        try:
            sock.connect((MANAGERADDR, PORTA))
        except:
            print "Impossível conectar no Manager"
            sys.exit(3)
        serialized = SerializeData(nlist)
        #payload = len(serialized)
        #payload += ":"
        #payload += serialized
        print "size of stream: %d" %(len(serialized))
        sock.sendall(serialized)
        
    finally:
        sock.close()
