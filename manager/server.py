#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from multiprocessing.connection import Listener
from common import *
from rpc import *

if __name__ == "__main__":
    from twisted.internet import reactor
    r = XmlHandler()
    reactor.listenTCP(PORT_BIND, server.Site(r))
    print "[*] Server Started"
    print "="*100
    reactor.run()
    