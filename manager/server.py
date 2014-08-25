#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# server.py
 
from multiprocessing.connection import Listener
from common import *
from datahandler import *
import threading
import thread

#def StartSock():
#    server_sock = Listener((BINDIP, PORTA))
#    conn = server_sock.accept()
#    data = conn.recv()
#    print type(data)
#    print "tamanho: %d"%(len(data))
#    ProcessData(Deserialize(data))

if __name__ == "__main__":
    #StartServer()

    from twisted.internet import reactor
    r = XmlHandler()
    reactor.listenTCP(PORTA, server.Site(r))
    print "Started XMLRPC"
    reactor.run()

    
