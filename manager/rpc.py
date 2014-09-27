#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.web import xmlrpc, server
from cqueue import *
from match import *
from common import *
from parser import *
import re

class XmlHandler(xmlrpc.XMLRPC):
    
    def xmlrpc_ping(self):
        return 1
    
    def xmlrpc_general(self,rcv_agent,rcv_domain,rcv_distro,rcv_distro_version,rcv_p_pid,rcv_p_name,rcv_p_uid,rcv_p_gid,rcv_p_rpm,rcv_p_dpkg,rcv_pf_path,rcv_pf_dac,rcv_pf_uid,rcv_pf_gid,rcv_p_args,rcv_p_tbanner,rcv_p_ubanner):
        #print "[+] Registrando Dados Gerais"
        if len(rcv_distro)==0 and len(rcv_p_name)==0:
            return False

        ParamDict={}
        ParamDict["agent"]=rcv_agent
        ParamDict["gateway"]=rcv_domain
        ParamDict["distro"]=rcv_distro
        ParamDict["distro_version"]=rcv_distro_version
        ParamDict["p_pid"]=rcv_p_pid
        ParamDict["p_name"]=rcv_p_name
        ParamDict["p_uid"]=rcv_p_uid
        ParamDict["p_gid"]=rcv_p_gid
        ParamDict["p_args"]=ParseArgs(rcv_p_args)
        ParamDict["pf_path"]=rcv_pf_path
        ParamDict["pf_dac"]=rcv_pf_dac
        ParamDict["pf_uid"]=rcv_pf_uid
        ParamDict["pf_gid"]=rcv_pf_gid

        rpm=False
        dpkg=False
        if str(rcv_p_rpm) != "nada" and len(rcv_p_rpm) >1:
            ParamDict["manager"]="RPM"
            ParamDict["pacote"]=rcv_p_rpm
            rpm=True

        if str(rcv_p_dpkg) != "nada" and len(rcv_p_dpkg) >1:
            ParamDict["manager"]="DPKG"
            ParamDict["pacote"]=rcv_p_dpkg
            dpkg=True

        if rpm == False and dpkg == False:
            ParamDict["manager"]=""
            ParamDict["pacote"]=""
        
        tbanner=""
        if rcv_p_tbanner != "" and len(str(rcv_p_tbanner)) >1:
            porta=rcv_p_tbanner.split(':')[0]
            try:
                tbanner=porta+":"+b64decode(rcv_p_tbanner.split(':')[1])
            except:
                tbanner=porta+":"+rcv_p_tbanner.split(':')[1]

        ubanner=""
        if rcv_p_ubanner != "" and len(str(rcv_p_ubanner)) >1:
            porta=rcv_p_ubanner.split(':')[0]
            try:
                ubanner=porta+":"+b64decode(rcv_p_ubanner.split(':')[1])
            except:
                ubanner=porta+":"+rcv_p_ubanner.split(':')[1]

        ParamDict["p_tcp_banner"]=tbanner
        ParamDict["p_udp_banner"]=ubanner
        recvdata.AddQueue(ParamDict)
        
        return True
        
    def xmlrpc_match(self):
        MatchData()
        return True

    def xmlrpc_ready(self):
        return state
    
    def xmlrpc_Fault(self):
        raise xmlrpc.Fault(123, "Erro.")











