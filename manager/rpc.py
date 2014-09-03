#!/usr/bin/env python
# -*- coding: utf-8 -*-
import common
from twisted.web import xmlrpc, server
from cqueue import *


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

        ParamDict={}
        ParamDict["agent"]=rcv_agent
        ParamDict["gateway"]=rcv_domain
        ParamDict["distro"]=rcv_distro
        ParamDict["distro_version"]=rcv_distro_version
        ParamDict["p_pid"]=rcv_p_pid
        ParamDict["p_name"]=rcv_p_name
        ParamDict["p_uid"]=rcv_p_uid
        ParamDict["p_gid"]=rcv_p_gid
        ParamDict["p_args"]=rcv_p_args
        ParamDict["p_rpm"]=rcv_p_rpm
        ParamDict["p_dpkg"]=rcv_p_dpkg
        ParamDict["pf_path"]=rcv_pf_path
        ParamDict["pf_dac"]=rcv_pf_dac
        ParamDict["pf_uid"]=rcv_pf_uid
        ParamDict["pf_gid"]=rcv_pf_gid
        ParamDict["tbanner"]=rcv_p_tbanner
        ParamDict["ubanner"]=rcv_p_ubanner


        print "  + Agente: "+ ParamDict["agent"]
        print "  + Gateway: "+ ParamDict["gateway"]
        print "  + Distro: "+ str(ParamDict["distro"])
        print "  + Distro Version: "+ str(ParamDict["distro_version"])
        print "  + Pid: "+ str(ParamDict["p_pid"])
        print "  + Processo: " +ParamDict["p_name"]
        print "  + UID do Processo: " +str(ParamDict["p_uid"])
        print "  + GID do Processo: " +str(ParamDict["p_gid"])
        print "  + Argumentos do Processo: " +ParamDict["p_args"]
        print "  + Pacote RPM: " +ParamDict["p_rpm"]
        print "  + Pacote DPKG: " +ParamDict["p_dpkg"]
        print "  + Patch do binário do processo: " +ParamDict["pf_path"]
        print "  + Dac do binário do processo: " +str(ParamDict["pf_dac"])
        print "  + Uid do binário do processo: "+str(ParamDict["pf_uid"])
        print "  + Gid do binário do processo: " +str(ParamDict["pf_gid"])
        print "  + Banner TCP do processo: " +ParamDict["tbanner"]
        print "  + Banner UDP do processo: " +ParamDict["ubanner"]

        pqueue.append(ParamDict)
        
        return True
    
    def xmlrpc_Fault(self):
        raise xmlrpc.Fault(123, "Erro.")











