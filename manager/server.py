#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# server.py
 
import socket
import select
import config as cfg
import Queue
from threading import Thread
from time import sleep
from random import randint
import sys
from common import *
from datahandler import *
 
class DoThread(Thread):
    def __init__(self):
        super(DoThread, self).__init__()
        self.running = True
        self.fila = Queue.Queue()
 
    def add(self, data):
        self.fila.put(data)
 
    def stop(self):
        self.running = False
 
    def run(self):
        fila = self.fila
        while self.running:
            try:
                # block for 5 seconds :
                value = fila.get(block=True, timeout=5)
                HandleStream(value)
            except Queue.Empty:
                #sys.stdout.write('.')
                #sys.stdout.flush()
                continue
    
        if not fila.empty():
            print "Elements left in the queue:"
            while not fila.empty():
                print fila.get()

t = DoThread()
t.start()

 
def StartServer():
    s = socket.socket()
    host = BINDIP
    port = PORTA
    s.bind((host, port))
    s.listen(5)
    while True:
        try:
            client, addr = s.accept()
            ready = select.select([client,],[], [],2)
            if ready[0]:
                data = client.recv(BUFSIZE)
                t.add(data)
        except:
            break
    Sair()
 
def Sair():
    t.stop()
    t.join()


if __name__ == "__main__":
    StartServer()



    
