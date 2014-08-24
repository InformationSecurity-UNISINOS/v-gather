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
        #SendData(p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid)
        p_tcp_l = item.getDaemonTcp()
        #TCP port: 0.0.0.0:8005,0.0.0.0:8009,0.0.0.0:8080,
        #TCP FP: {8080: u'Apache Tomcat/Coyote JSP engine', 8009: u'Apache Jserv', 8005: ''}
        
        for svc in p_tcp_l.split(','):
            try:
                ip = svc.split(':')[0]
                porta = svc.split(':')[1]
                p_tcp_fp_l={}
                p_tcp_fp_l = item.getDaemonTcpFp()
                print p_tcp_fp_l.get(int(porta))
                print p_tcp_fp_l.get(str(porta))
                
                #for key, value in p_tcp_fp_l.iteritems():
                #   if int(key) == int(porta):
                #        listfp=ip+":"+porta+":"value
                print "*"*50
                
            except:
                continue

 
            
        
        
        p_udp_l = item.getDaemonUdp()
        p_udp_fp_l = item.getDaemonUdpFp()

        
        
        continue
    sys.exit(1)
        
        # converter pra base64 e no server restaurar e fazer update no banco
        # enviar payload no formato:
        # pid:base64_encoded
 #       p_args = item.getDaemonArgs()
        
        # converter pra base64 e no server restaurar e fazer update no banco
        # enviar payload no formato:
        # pid:base64_encoded
 #       iof=item.getDaemonIo()
 #       for token in iter(iof):
 #           if token.getUname() == None:
 #               user=token.getUid()
 #           else:
 #               user=token.getUname()

 #            if token.getGname() == None:
 #               group=token.getGid()
 #           else:
 #               group=token.getGname()
 #           SendData()
 #           print "\t%s\t%s\t%d\t%s" %(user,group,token.getDac(),token.getFile())
        
        



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









