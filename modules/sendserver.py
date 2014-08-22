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
    client = Client((MANAGERADDR, PORTA))
    serialized = SerializeData(nlist)
    print "size of stream: %d" %(len(serialized))
    client.send(serialized)
    client.close()