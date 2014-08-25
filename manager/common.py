# -*- coding: utf-8 -*-
'''
' DEFINICOES GLOBAIS 
'''
BUFSIZE=200000
PORTA=3339
BINDIP="0.0.0.0"


from Queue import Queue
RequestQueue = Queue(maxsize=0)

'''
 Recebe Registro de Agente
 Toda comunicação é conferida através da confirmação do agente
 Requisições de todos os agentes entram para uma queue
 Essa queue é processada e registrada vinculada ao endereço ip do agente (profile por servidor)
 
 Agent: É o endereço IP do agente remoto, para identificar de qual servidor veio a request.
 Domain: Para registrar de qual empresa veio a request, para agrupar todos os IPS pertinentes.
 p_pid: vai identificar qual é o processo, dentro do servidor em questão, a qual cada item se refere
 
 
 
 
'''

from twisted.web import xmlrpc, server
class XmlHandler(xmlrpc.XMLRPC):
    def xmlrpc_register(self,address,domain,code):
        agent = code
        agent_address = address
        agent_domain = domain
        return True
    
    def xmlrpc_ping(self):
        return True
    
    def xmlrpc_banner(self,rcv_agent,rcv_domain,rcv_p_pid,rcv_p_banner):
        print "[+] Registrando Banner"

        agent = rcv_agent
        domain = rcv_domain
        p_pid = rcv_p_pid
        p_banner = rcv_p_banner
        
        print "  + Servidor: %s" %agent
        print "  + Domain: %s" %domain
        print "  + PID: %s" %str(p_pid)
        print "    - Banner: %s"%p_banner
        return True
    
    def xmlrpc_args(self,rcv_agent,rcv_domain,rcv_p_pid,rcv_p_arg):
        print "[+] Registrando Argumentos"
        agent = rcv_agent
        domain = rcv_domain
        p_pid = rcv_p_pid
        p_args = rcv_p_arg
        
        print "  + Servidor: %s" %agent
        print "  + Domain: %s" %domain
        print "  + PID: %s" %str(p_pid)
        print "    - Argumentos: %s" %p_args
        return True
    
    def xmlrpc_general(self,rcv_agent,rcv_domain,rcv_p_pid,rcv_p_name,rcv_p_uid,rcv_p_gid,rcv_p_rpm,rcv_p_dpkg,rcv_pf_path,rcv_pf_dac,rcv_pf_uid,rcv_pf_gid):
        print "[+] Registrando Dados Gerais"
        agent = rcv_agent
        domain = rcv_domain
        p_pid = rcv_p_pid
        p_name = rcv_p_name
        p_uid = rcv_p_uid
        p_gid = rcv_p_gid
        p_rpm = rcv_p_rpm
        p_dpkg = rcv_p_dpkg
        pf_path = rcv_pf_path
        pf_dac = rcv_pf_dac
        pf_uid = rcv_pf_uid
        pf_gid = rcv_pf_gid
        
        print "  + Servidor: %s" %agent
        print "  + Domain: %s" %domain
        print "  + PID: %s" %str(p_pid)
        print "    - Processo: %s" %p_name
        print "    - P.UID: %s" %p_uid
        print "    - P.GID: %s" %p_gid
        print "    - RPM: %s" %p_rpm
        print "    - DPKG: %s" %p_dpkg
        print "    - Path: %s" %pf_path
        print "    - File Uid: %s" %pf_uid
        print "    - File Gid: %s" %pf_gid
        return True
    
    def xmlrpc_ofiles(self,rcv_agent,rcv_domain,rcv_p_pid,rcv_pf_io):
        print "[+] Registrando Arquivos Abertos"
        agent = rcv_agent
        domain = rcv_domain
        p_pid = rcv_p_pid
        pf_io = rcv_pf_io
        
        print "  + Servidor: %s" %agent
        print "  + Domain: %s" %domain
        print "  + PID: %s" %str(p_pid)
        print "    - Arquivo IO: %s" %pf_io
        return True

    def xmlrpc_Fault(self):
        """
        Raise a Fault indicating that the procedure should not be used.
        """
        raise xmlrpc.Fault(123, "The fault procedure is faulty.")











