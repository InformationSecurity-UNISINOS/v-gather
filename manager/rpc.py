#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.web import xmlrpc, server
from cqueue import *
from match import *
from common import *
from parser import *


'''
 Recebe Registro de Agente
 Toda comunicação é conferida através da confirmação do agente
 Requisições de todos os agentes entram para uma queue
 Essa queue é processada e registrada vinculada ao endereço ip do agente (profile por servidor)
 
 Agent: É o endereço IP do agente remoto, para identificar de qual servidor veio a request.
 Domain: Para registrar de qual empresa veio a request, para agrupar todos os IPS pertinentes.
 p_pid: vai identificar qual é o processo, dentro do servidor em questão, a qual cada item se refere
 

'''

class XmlHandler(xmlrpc.XMLRPC):
    def xmlrpc_register(self,address,domain,code):
        agent = code
        agent_address = address
        agent_domain = domain
        return True
    
    def xmlrpc_ping(self):
        return 1
    
    def xmlrpc_general(self,rcv_agent,rcv_domain,rcv_distro,rcv_distro_version,rcv_p_pid,rcv_p_name,rcv_p_uid,rcv_p_gid,rcv_p_rpm,rcv_p_dpkg,rcv_pf_path,rcv_pf_dac,rcv_pf_uid,rcv_pf_gid,rcv_p_args,rcv_p_tbanner,rcv_p_ubanner):
        print "[+] Registrando Dados Gerais"
        print "----"
        print "rcv_p_pid" + str(rcv_p_pid)
        print "rcv_p_name: " +rcv_p_name
        print "rcv_p_tbanner/size: %s/%s" %(rcv_p_tbanner,len(rcv_p_tbanner))
        print "rcv_p_ubanner/size: %s/%s" %(rcv_p_ubanner,len(rcv_p_ubanner))
        print "----" 

        if rcv_p_tbanner is not "":
            print "rcv_p_tbanner is not blank"
            tcp_ports_total=ParseBanner(rcv_p_tbanner,0)[0]
            for port_pos in range(0,tcp_ports_total):
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
                i,ParamDict["p_tcp_banner"]=ParseBanner(rcv_p_tbanner,port_pos)
                ParamDict["p_udp_banner"]=""
                AddQueue(ParamDict)
                print "pos: "+str(port_pos)
                print "pid: %s" %str(ParamDict["p_pid"])
                print "pname: %s" %ParamDict["p_name"]
                print "p_tcp_banner: %s" %str(ParamDict["p_tcp_banner"])
                print "*"*50
        elif rcv_p_ubanner is not "":
            print "rcv_p_ubanner is not blank"
            udp_ports_total=ParseBanner(rcv_p_ubanner,0)[0]
            for port_pos in range(0,udp_ports_total):
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
                i,ParamDict["p_udp_banner"]=ParseBanner(rcv_p_ubanner,port_pos)
                AddQueue(ParamDict)
                print "pos: "+str(port_pos)
                print "pid: %s" %str(ParamDict["p_pid"])
                print "pname: %s" %ParamDict["p_name"]
                print "p_tcp_banner: %s" %str(ParamDict["p_udp_banner"])
                print "*"*50
        else:
            print "rcv_p_ubanner and rcv_p_tbanner is blank"
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
            try:
                print "pos: "+str(port_pos)
            except:
                pass
            print "pid: %s" %str(ParamDict["p_pid"])
            print "pname: %s" %ParamDict["p_name"]
            print "p_tcp_banner: %s" %str(ParamDict["p_tcp_banner"])
            print "p_udp_banner: %s" %str(ParamDict["p_udp_banner"])
            print "*"*50

        #MatchData()
        return True
    
    def xmlrpc_Fault(self):
        raise xmlrpc.Fault(123, "Erro.")











