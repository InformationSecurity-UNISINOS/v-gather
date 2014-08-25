#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is the main file 
Working with packages: https://docs.python.org/2/tutorial/modules.html - item 6.4
'''
import sys
from modules.mfs import *
from modules.mvram import *
from common import *
from modules.sendserver import *
from base64 import *
from rbase import *
import getopt

def usage():
    print "%s <opcao> " %(sys.argv[0])
    print "\t-s\tMostrar estado da base de casos"
    print "\t-a\tAnalisar ambiente"
    print "\t-r\tRegistrar um novo caso (interativo)"
    print "\t-c arquivo.txt\tCarregar novo caso a partir de um arquivo"
    print "\t-e arquivo.txt\tExportar base de casos para texto plano"

def StartScan():
    GetDaemons()
    #nlist=[]
    #nlist=OpenBase()
    group=user=token=""
    
    for item in nlist:
        p_pid = item.getDaemonPid()
        p_name = item.getDaemon()
        p_uid = item.getDaemonUid()
        p_gid = item.getDaemonGid()
        p_rpm = item.getDaemonRpm()
        p_dpkg = item.getDaemonDpkg()
        pf_path = item.getFilePath()
        pf_dac = item.getFileDac()
        pf_uid = item.getFileUid()
        pf_gid = item.getFileGid()
        buf = p_pid+":"+p_name+":"+p_uid+":"+p_gid+":"+p_rpm+":"+p_dpkg+":"+pf_path+":"+pf_dac+":"+pf_uid+":"+pf_gid
        SendData(GENERAL,buf)
        
        p_tcp_l = item.getDaemonTcp()
        for svctcp in p_tcp_l.split(','):
            try:
                ip = svctcp.split(':')[0]
                porta = svctcp.split(':')[1]
                p_tcp_fp_l={}
                p_tcp_fp_l = item.getDaemonTcpFp()
                banner = base64.b64encode(p_tcp_fp_l.get(int(porta)))
                service = p_pid+"tcp:"+ip+":"+porta+":"+banner
                SendData(BANNER,service)
            
            except:
                continue
    
        p_udp_l = item.getDaemonUdp()
        for svcudp in p_udp_l.split(','):
            try:
                ip = svcudp.split(':')[0]
                porta = svcudp.split(':')[1]
                p_tcp_fp_l={}
                p_udp_fp_l = item.getDaemonUdpFp()
                banner = base64.b64encode((p_udp_fp_l.get(int(porta)))
                service = p_pid+"udp:"+ip+":"+porta+":"+banner
                SendData(BANNER,service)
            except:
                continue

        
        # converter pra base64 e no server restaurar e fazer update no banco
        # enviar payload no formato:
        # pid:base64_encoded
        p_args = p_pid+":"+base64.b64encode(item.getDaemonArgs())
        SendData(ARGS,p_args)
        
        
        
        # converter pra base64 e no server restaurar e fazer update no banco
        # enviar payload no formato:
        # pid:base64_encoded
        iof=item.getDaemonIo()
        for token in iter(iof):
            if token.getUname() == None:
                user=token.getUid()
            else:
                user=token.getUname()

             if token.getGname() == None:
                group=token.getGid()
            else:
                group=token.getGname()
            
            buf = user+":"+group+":"+token.getDac()+":"+token.getFile()
            pf_io = p_pid+":"+base64.b64encode(buf)
            SendData(OFILES,pf_io)



        #print "Daemon: %s"  %item.getDaemon()
        #print "Pid: %d"  %item.getDaemonPid()
        #print "Daemon Uid: %d" %item.getDaemonUid()
        #print "Daemon Gid: %d" %item.getDaemonGid()
        #print "Daemon IO Files:"
        #iof=item.getDaemonIo()
        #for token in iter(iof):
        #    if token.getUname() == None:
        #        user=token.getUid()
        #    else:
        #        user=token.getUname()
        #
        #    if token.getGname() == None:
        #        group=token.getGid()
        #    else:
        #        group=token.getGname()
        #    print "\t%s\t%s\t%d\t%s" %(user,group,token.getDac(),token.getFile())
        #
        #print "Daemon Args: %s" %item.getDaemonArgs()

        #print "Daemon TCP port: %s" %item.getDaemonTcp()
        #print "Daemon TCP FP: %s" %item.getDaemonTcpFp()

        #print "Daemon UDP port: %s" %item.getDaemonUdp()
        #print "Daemon UDP FP: %s" %item.getDaemonUdpFp()
        #print "Daemon file Path: %s" %item.getFilePath()
        #print "Daemon Rpm Package: %s" %item.getDaemonRpm()
        #print "Daemon Dpkb Package: %s" %item.getDaemonDpkg()
        #print "Daemon File Dac: %d" %item.getFileDac()
        #print "Daemon File Uid: %d" %item.getFileUid()
        #print "Daemon File Gid: %d" %item.getFileGid()
        #print "*"* 150


def ShowDBStatus():
    print "status beleza"
    print "existem x casos na base"

def RegisterCase():
    print "beleza, vamos registrar"
    print "Serviço: "
    print "Uid do processo: "
    print "Gid do processo: "
    print "Arquivos IO: "
    print "Argumentos do processo: "
    print "Portas TCP: "
    print "Portas UDP: "
    print "Fingerprint: "
    print "Arquivo do serviço: "
    print "Permissões DAC do arquivo do processo: "
    print "Uid do arquivo do processo: "
    print "Gid do arquivo do processo: "
    print "RPM: "
    print "DPKG: "

def LoadCaseFromFile(casefile):
    print "beleza, vou carregar o caso"

def ExportCaseToFile(outputfile):
    print "Beleza, vou exportar os casos pro arquivo"
    data=[]
    data=OpenBase()
    fd=open(outputfile,'w')
    fd.write("Daemon: %s"%(item.getDaemon()))

def main():
    print "v-gather CBR"
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "sarc:e:h")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for opcao, argumento in opts:
        if opcao == "-s":
            ShowDBStatus()
        if opcao == "-h":
            usage()
        if opcao == "-a":
            StartScan()
        if opcao == "-r":
            RegisterCase()
        if opcao == "-c":
            LoadCaseFromFile(argumento)
        if opcao == "-e":
            ExportCaseToFile(argumento)


if __name__ == "__main__":
    main()









