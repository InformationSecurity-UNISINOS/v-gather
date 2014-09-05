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
from queue import *
import getopt

def usage():
    print "%s <opcao> " %(sys.argv[0])
    print "\t-t\tTestar comunicação com o manager"
    print "\t-a\tAnalisar ambiente"
    print "\t-h\tMostrar este help"

def StartScan():
    domain,server=GetHostNetwork()
    GetDaemons()
    group=user=token=""
    
    for item in nlist:
        p_pid = item.getDaemonPid()
        p_name = item.getDaemon()
        p_uid = str(item.getDaemonUid())
        p_gid = str(item.getDaemonGid())
        p_rpm = item.getDaemonRpm()
        if p_rpm == None:
            p_rpm="nada"
        p_dpkg = item.getDaemonDpkg()
        if p_dpkg == None:
            p_dpkg="nada"
        pf_path = item.getFilePath()
        if pf_path == None:
            pf_path="nada"
        pf_dac = str(item.getFileDac())
        pf_uid = str(item.getFileUid())
        pf_gid = str(item.getFileGid())
        p_args = b64encode(item.getDaemonArgs())
        #SendArgs(server,domain,p_pid,p_args)

        p_tcp_l = item.getDaemonTcp()
        print "DEBUG1: >>>>>>>>>>>>>>>>>>>>>>>>>>>>> p_tcp_l:" +p_tcp_l
        tbuf=tbanner=""
        tcp_ports=0
        if p_tcp_l is not "":
            tloop=0
            for svctcp in p_tcp_l.split(','):
                try:
                    ip = svctcp.split(':')[0]
                    porta = svctcp.split(':')[1]
                    if porta == 80:
                        print "DEBUG>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PORTA 80"
                    p_tcp_fp_l={}
                    p_tcp_fp_l = item.getDaemonTcpFp()
                    fp_item=p_tcp_fp_l.get(int(porta))
                    if fp_item is not '' and fp_item is not None:
                        '''
                            Se o servico tiver muitas portas,
                            aproveitarei somente o banner da primeira, os demais 
                            eu presumo que sao iguais.
                            Porém eu nao saio do loop, e aproveito o 
                            tloop pra contabilizar quantas portas abertas
                            esse serviço tem.
                        '''
                        if tloop==1: 
                            banner=b64encode(fp_item)
                            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>banner: "+banner
                            tbuf="tcp:"+ip+":"+porta+":"+banner
                        tloop+=1


                        tem que refazer esse algoritmo...
                        tem servicos (apache) que nao estao pegando o banner... nem portas nem nada..
                        tem algum bug
                except:
                    continue


        p_udp_l = item.getDaemonUdp()
        ubuf=ubanner=""
        udp_ports=0
        if p_udp_l is not "":
            uloop=0
            for svcudp in p_udp_l.split(','):
                try:
                    ip = svcudp.split(':')[0]
                    porta = svcudp.split(':')[1]
                    p_tcp_fp_l={}
                    p_udp_fp_l = item.getDaemonUdpFp()
                    fp_item=p_udp_fp_l.get(int(porta))
                    if fp_item is not '' and fp_item is not None:
                        if uloop==1:
                            banner = b64encode(fp_item)
                            ubuf="udp:"+ip+":"+porta+":"+banner
                        uloop+=1
                except:
                    continue

        # soh aproveita o banner udp se o banner udp nao existir
        if tbuf is not "":
            tbanner=tbuf+":"+str(tloop)

        if ubuf is not "":
            ubanner=ubuf+":"+str(uloop)

        if PingManager()==1:
            print "Server: "+server
            print "Gw: "+domain
            print "Distro: "+GetLinuxDist(DIST_NAME)
            print "DistroVer: "+GetLinuxDist(DIST_VER)
            print "Pid: "+str(p_pid)
            print "PName: "+p_name
            print "Puid: "+str(p_uid)
            print "Pgid: "+str(p_gid)
            print "Prmp: "+p_rpm
            print "Pdpkg: "+p_dpkg
            print "FPath: "+pf_path
            print "FDac: "+str(pf_dac)
            print "Fuid: "+str(pf_uid)
            print "Fgid: "+str(pf_gid)
            print "Fargs: "+p_args
            print "Tbanner: "+tbanner
            print "Ubanner: "+ubanner
            SendData(server,domain,GetLinuxDist(DIST_NAME),GetLinuxDist(DIST_VER),p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args,tbanner,ubanner)
        else:
            print "[x] Manager offline"
        

def main():
    print "v-gather CBR"
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ath")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for opcao, argumento in opts:
        if opcao == "-t":
            if PingManager() == 1:
                print "[+] Manager Online"
            else:
                print '[+] Manager Offline'
        if opcao == "-h":
            usage()
        if opcao == "-a":
            StartScan()
        


if __name__ == "__main__":
    main()









