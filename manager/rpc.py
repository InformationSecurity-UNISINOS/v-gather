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
        ready=False
        #if DbCheckAgent(rcv_agent) == False:    # authorized agents only
        #        return False
        if len(rcv_distro)==0 and len(rcv_p_name)==0:
            return False

        if rcv_p_tbanner is not "":
            tcp_ports_total=ParseBanner(rcv_p_tbanner,0)[0]
            for port_pos in range(0,tcp_ports_total):
                tbanner=ParseBanner(rcv_p_tbanner,port_pos)[1]  
            
                if CheckKnownTcpPort(tbanner) == False:
                    ready=True
                    ParamDict={}
                    try:
                        ParamDict["p_tcp_banner"]=tbanner.split(':')[0]+":"+b64decode(tbanner.split(':')[1])
                    except:
                        ParamDict["p_tcp_banner"]=tbanner
                    ParamDict["p_udp_banner"]=""
                    ParamDict["agent"]=rcv_agent
                    ParamDict["gateway"]=rcv_domain
                    ParamDict["distro"]=rcv_distro
                    ParamDict["distro_version"]=rcv_distro_version
                    ParamDict["p_pid"]=rcv_p_pid
                    ParamDict["p_name"]=rcv_p_name
                    ParamDict["p_uid"]=rcv_p_uid
                    ParamDict["p_gid"]=rcv_p_gid
                    ParamDict["p_args"]=ParseArgs(rcv_p_args)
                    ParamDict["p_rpm"]=rcv_p_rpm
                    ParamDict["p_dpkg"]=rcv_p_dpkg
                    ParamDict["pf_path"]=rcv_pf_path
                    ParamDict["pf_dac"]=rcv_pf_dac
                    ParamDict["pf_uid"]=rcv_pf_uid
                    ParamDict["pf_gid"]=rcv_pf_gid
                    
                    AddQueue(ParamDict)
                else: 
                    pass # to be explicit on this case

        elif rcv_p_ubanner is not "":
            udp_ports_total=ParseBanner(rcv_p_ubanner,0)[0]
            for port_pos in range(0,udp_ports_total):
                ubanner=ParseBanner(rcv_p_ubanner,port_pos)[1]   #ainda em base64
                
                if CheckKnownUdpPort(ubanner) == False:
                    ready=True
                    ParamDict={}
                    try:
                        ParamDict["p_udp_banner"]=ubanner.split(':')[0]+":"+b64decode(ubanner.split(':')[1])
                    except:
                        ParamDict["p_udp_banner"]=ubanner
                    ParamDict["p_tcp_banner"]=""
                    ParamDict["agent"]=rcv_agent
                    ParamDict["gateway"]=rcv_domain
                    ParamDict["distro"]=rcv_distro
                    ParamDict["distro_version"]=rcv_distro_version
                    ParamDict["p_pid"]=rcv_p_pid
                    ParamDict["p_name"]=rcv_p_name
                    ParamDict["p_uid"]=rcv_p_uid
                    ParamDict["p_gid"]=rcv_p_gid
                    ParamDict["p_args"]=ParseArgs(rcv_p_args)
                    ParamDict["p_rpm"]=rcv_p_rpm
                    ParamDict["p_dpkg"]=rcv_p_dpkg
                    ParamDict["pf_path"]=rcv_pf_path
                    ParamDict["pf_dac"]=rcv_pf_dac
                    ParamDict["pf_uid"]=rcv_pf_uid
                    ParamDict["pf_gid"]=rcv_pf_gid
                    AddQueue(ParamDict)
                else:
                    pass
        else:
            ready=True
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
            ParamDict["p_rpm"]=rcv_p_rpm
            ParamDict["p_dpkg"]=rcv_p_dpkg
            ParamDict["pf_path"]=rcv_pf_path
            ParamDict["pf_dac"]=rcv_pf_dac
            ParamDict["pf_uid"]=rcv_pf_uid
            ParamDict["pf_gid"]=rcv_pf_gid
            ParamDict["p_tcp_banner"]=""
            ParamDict["p_udp_banner"]=""
            AddQueue(ParamDict)

        if ready==True:
            MatchData()
        return True
    
    def xmlrpc_Fault(self):
        raise xmlrpc.Fault(123, "Erro.")











