# -*- coding: utf-8 -*-
import subprocess
import psutil
import platform
from common import *
from treedict import TreeDict
import mfs
from mnet import *
import sys

'''
'   ChkLinuxDist: Verifica Distribuição Linux 
'   Argumentos: Nome da Distribuição a verificar
'               Versão da distribuição a verificar
'               Usar ou não o modo verbose.
'   Retorno:    
'               Caso apenas o nome da distribuição coincida o valor retornado será 1
'               Caso o nome da distribuição e a versão coincidam, o retorno será 2
'               Caso nada coincida, o retorno será zero
'
'''
def CheckLinuxDist(distname,distver,verbose):
    
    ret=0
    dist=platform.linux_distribution()
    if distname in dist[0]:
        ret=1
    if distver in dist[1]:
        ret=2
    if verbose == True:
        if ret == 0:
            print "<+> Distribuição diferente"
        if ret == 1:
            print "<+> Distribuição igual, versão diferente"
        if ret == 2:
            print "<+> Distribuição igual, versão igual"
            
    return ret

'''
'' Retorna qual distribuição (sem versão) Linux está em uso
''
'''
def GetLinuxDist(opt):
    if opt == DIST_NAME:
        return platform.linux_distribution()[0]
    if opt == DIST_VER:
        return platform.linux_distribution()[1]

'''
'' Captura o output de algum comando de sistema
''
'''
#def CheckCmdOutput(cmd,arguments,argtok,verbose):
#    args=[]
#    alist=arguments.split(argtok)
#    for a in alist:
#        args.append(a)

#    p = subprocess.Popen([cmd ] + args, stdout=subprocess.PIPE)
#    out, err = p.communicate()
#    return out

'''
'' Verifica processos em execução
''
'''
#def CheckRunningProc(procname,verbose):
#    ret=[]
#    pids=psutil.pids()
#    for pid in pids:
#        p = psutil.Process(pid)
#        cmdline=p.cmdline()
#        if len(cmdline) < 2:
#            cmdline=p.name()
#
#        if procname in cmdline:
#            ret.append(cmdline)
#        else:
#            if any(procname in s for s in cmdline):
 #               ret.append(cmdline)
#
#    if len(ret)>0:
#        return ret
#    else:
#        return None

'''
'' Verifica arquivos abertos por processos
''
'''
def GetProcArgs(pid):
    args=""
    p=psutil.Process(pid)
    first=0
    for tokens in iter(p.cmdline()):
        if first==1:
            args+=tokens + " "
        first=1
    return args


def GetProcCmd(pid):
    p=psutil.Process(pid)
    daemon = p.exe()
    if len(daemon) == 0:
        daemon=p.name()
    return daemon

def GetDaemons():
    pids=psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
        except:
            continue
        daemon = p.name()
        if len(daemon) == 0:
                daemon=p.exe()
        u_real,u_eff,u_saved = p.uids()
        g_real,g_eff,g_saved = p.gids()
        udp_port=tcp_port=""
        nodo=DaemonInfo()
        
        for x in p.connections('udp'):
                if x.status == 'LISTEN' or x.status == 'NONE':
                        ipaddr=x.laddr[0]
                        udpport=x.laddr[1]
                        if CheckIpv6(ipaddr) == True:
                            ipaddr="0.0.0.0"
                        if udpport in svc_udp_checked.keys():
                            svc_ident=svc_udp_checked.get(udpport)
                        else:
                            svc_ident=CheckSvcFPrint(ipaddr,udpport,"UDP")
                            svc_udp_checked[udpport]=svc_ident
                        udp_port+=str(ipaddr)+":"+str(udpport)+","
                        nodo.svc_udp_fp[udpport]=svc_ident

        for x in p.connections('tcp'):
                svc={}
                if x.status == 'LISTEN' or x.status == 'NONE':
                        ipaddr=x.laddr[0]
                        tcpport=x.laddr[1]
                        if CheckIpv6(ipaddr) == True:
                            ipaddr="0.0.0.0"
                        # verifica se ja tem fingerprint desta porta
                        # se ja tiver registro, nao precisa scanear novamente
                        if tcpport in svc_tcp_checked.keys(): 
                            svc_ident=svc_tcp_checked.get(tcpport)
                        else:
                            svc_ident=CheckSvcFPrint(ipaddr,tcpport,"TCP")
                            svc_tcp_checked[tcpport]=svc_ident
                        tcp_port+=str(ipaddr)+":"+str(tcpport)+","
                        nodo.svc_tcp_fp[tcpport]=svc_ident

        nodo.daemon=daemon
        nodo.downer_uid=u_real
        nodo.downer_gid=g_real
        nodo.pid=pid
        nodo.args=GetProcArgs(pid)
        nodo.tcp=tcp_port
        nodo.udp=udp_port
        arq=GetProcCmd(pid)
        if GetLinuxDist(DIST_NAME).lower()=="debian":
            nodo.dpkg=mfs.FileToDpkg(arq)
        if GetLinuxDist(DIST_NAME).lower()=="centos":
            nodo.rpm=mfs.FileToRpm(arq)

        nodo.file_path=arq
        nodo.file_dac=mfs.GetDacMode(arq)
        owner=mfs.CheckIdOwner(arq)
        nodo.file_uid=owner[0]
        nodo.file_gid=owner[1]
        
        nlist.append(nodo)





