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

        p_tcp_l = item.getDaemonTcp()                   # recebe tcp:0.0.0.0:80
        banner=""
        tcp_pcount=0
        if p_tcp_l is not "" and p_tcp_l is not None:   # Se realmente recebeu uma tupla de porta aberta
            for svctcp in p_tcp_l.split(','):           # entao vamos tokenizar cada tupla separada por virgula (se tiver mais de1 porta aberta por processo)
                try:
                    ip=svctcp.split(':')[0]
                    porta=svctcp.split(':')[1]
                    p_tcp_fp_l={}
                    p_tcp_fp_l = item.getDaemonTcpFp()
                    fp_item=p_tcp_fp_l.get(int(porta))
                    #print "ip: " + ip + " porta: " + porta + " banner: " + fp_item 
                    banner=porta+":"+b64encode(fp_item) # porta:banner em base64 
                    tcp_pcount+=1
                except:
                    continue
        else:
            continue
        
        p_udp_l = item.getDaemonUdp()
        ubuf=ubanner=""
        udp_pcount=0
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
        if banner is not "":
            banner=banner+":"+str(tcp_pcount)

        if ubuf is not "":
            ubanner=ubuf+":"+str(uloop)

        if PingManager()==1:
            #print "Server: "+server
            #print "Gw: "+domain
            #print "Distro: "+GetLinuxDist(DIST_NAME)
            #print "DistroVer: "+GetLinuxDist(DIST_VER)
            #print "Pid: "+str(p_pid)
            #print "PName: "+p_name
            #print "Puid: "+str(p_uid)
            #print "Pgid: "+str(p_gid)
            #print "Prmp: "+p_rpm
            #print "Pdpkg: "+p_dpkg
            #print "FPath: "+pf_path
            #print "FDac: "+str(pf_dac)
            #print "Fuid: "+str(pf_uid)
            #print "Fgid: "+str(pf_gid)
            #print "Fargs: "+p_args
            #print "Tbanner: "+tbanner
            #print "Ubanner: "+ubanner
            while True:
                if ServerReady() == True:
                    SendData(server,domain,GetLinuxDist(DIST_NAME),GetLinuxDist(DIST_VER),p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args,banner,ubanner)
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









