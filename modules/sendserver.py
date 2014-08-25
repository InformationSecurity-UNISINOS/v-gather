#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
from common import *

def SendData(mode,string):
    import xmlrpclib
    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    if mode == OFILES:
        s.ofiles(string)
    if mode == BANNER:
        s.banner(string)
    if mode == ARGS:
        s.args(string)
    if mode == GENERAL:
        s.general(string)
    
    #s.echo(string)