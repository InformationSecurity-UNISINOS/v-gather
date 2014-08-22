#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
import common


def SerializeData(data):
    import pickle
    import pickletools
    serialized=pickle.dumps(data)
    return serialized

def CompressData(data):
    import zlib
    cdata = zlib.compress(data)
    return cdata

def SendData(data):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((MANAGER, PORTA))
    serialized = SerializeData(data)
    compressed = CompressData(serialized)
    sock.sendall(compressed);

finally:
    sock.close()
