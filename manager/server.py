#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# server.py
 
from multiprocessing.connection import Listener
from common import *
from datahandler import *
import threading
import thread

if __name__ == "__main__":
    from twisted.internet import reactor
    r = XmlHandler()
    reactor.listenTCP(PORTA, server.Site(r))
    print "Started XMLRPC"
    reactor.run()

    
