#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from common import *
import xmlrpclib

def SendData(manageraddr,server,domain,distro,distro_version,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args,tbanner,ubanner):
    remote_server="http://"+str(manageraddr)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    s.general(server,domain,distro,distro_version,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args,tbanner,ubanner)

def PingManager(manageraddr):
    remote_server="http://"+str(manageraddr)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    ret=s.ping()
    return ret

def SendMatchCmd(manageraddr):
    remote_server="http://"+str(manageraddr)+":"+str(PORTA)
    s = xmlrpclib.Server(remote_server)
    ret=s.match()
    return ret