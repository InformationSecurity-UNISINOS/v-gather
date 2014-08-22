#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# server.py
 
from multiprocessing.connection import Listener
from common import *
from datahandler import *

def StartServer():
#    server_sock = Listener((BINDIP, PORTA))
#    conn = server_sock.accept()
#    data = conn.recv()
#    print type(data)
#    print "tamanho: %d"%(len(data))
#    ProcessData(Deserialize(data))
# ISSO A CIMA FUNCIONA


    serversock = Listener((BINDIP, PORTA))
    #serversock.bind(ADDR)
    #serversock.listen(2)

    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(thandler, (clientsock, addr))



def thandler(clientsock,addr):
    while 1:
        data = clientsock.recv()
        if not data:
            break
        print type(data)
        print "tamanho: %d"%(len(data))

    clientsock.close()






if __name__ == "__main__":
    StartServer()



    
