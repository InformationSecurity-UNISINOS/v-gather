#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from common import *
import xmlrpclib

def SendData(server,domain,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args):
    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    s.general(server,domain,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args)

#def SendGeneral(server,domain,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid):
#    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
#    s = xmlrpclib.Server(remote_server)
#    s.general(server,domain,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid)
    
#def SendBanner(server,domain,p_pid,buf):
#    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
#    s = xmlrpclib.Server(remote_server)
#    s.banner(server,domain,p_pid,buf)
    
#def SendOfiles(server,domain,p_pid,pf_io):
#    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
#    s = xmlrpclib.Server(remote_server)
#    s.ofiles(server,domain,p_pid,pf_io)

#def SendArgs(server,domain,p_pid,p_args):
#    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
#    s = xmlrpclib.Server(remote_server)
#    s.args(server,domain,p_pid,p_args)

def PingManager():
    remote_server="http://"+str(MANAGERADDR)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    ret=s.ping()
    return ret
