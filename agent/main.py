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
import getopt

def usage():
    print "%s <opcao>" %(sys.argv[0])
    print "\t-t\tTestar comunicação com o manager"
    print "\t-a\tAnalisar ambiente <endereço ip do manager>"
    print "\t-d\tModo dry-run (Roda local, exibe, mas nao submete ao manager)"
    print "\t-h\tMostrar este help"

def StartScan(Dry,manageraddr):
    domain,server=GetHostNetwork()
    GetDaemons()
    group=user=token=""
    sent_count=0
    
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

        if Dry==True:
            print "GNU/LINUX DIST: " +str(GetLinuxDist(DIST_NAME))
            print "DIST VERSION: " +str(GetLinuxDist(DIST_VER))
            print "PROCESS PID: " +str(p_pid)
            print "PROCESS NAME: " +str(p_name)
            print "PROCESS UID: " +str(p_uid)
            print "PROCESS GID: " +str(p_gid)
            print "PROCESS RPM: " +str(p_rpm)
            print "PROCESS DPKG: " +str(p_dpkg)
            print "PROCESS ARGS: " +str(item.getDaemonArgs())
            print "PROCESS FILE PATH: " +str(pf_path)
            print "PROCESS FILE UID: " +str(pf_uid)
            print "PROCESS FILE GID: " +str(pf_gid)
            print "PROCESS FILE DAC: " +str(pf_dac)

        p_tcp_l = item.getDaemonTcp()                   # recebe 0.0.0.0:80
        tcp_banner=""
        tcp_pcount=0
        if p_tcp_l is not "" and p_tcp_l is not None:   # Se realmente recebeu uma tupla de porta aberta
            for svctcp in p_tcp_l.split(','):           # entao vamos tokenizar cada tupla separada por virgula (se tiver mais de1 porta aberta por processo)
                try:
                    ip=svctcp.split(':')[0]
                    porta=svctcp.split(':')[1]
                    p_tcp_fp_l={}
                    p_tcp_fp_l=item.getDaemonTcpFp()
                    fp_item=p_tcp_fp_l.get(int(porta))
                    # print "ip: " + ip + " porta: " + porta + " banner: " + fp_item 
                    if Dry==True:
                         print "PROCESS TCP FINGERPRINT: " +str(porta)+":"+str(fp_item)
                    tcp_banner=tcp_banner+porta+":"+b64encode(fp_item) + ":" # porta:banner em base64 
                    tcp_pcount+=1
                except:
                    continue


        p_udp_l = item.getDaemonUdp()                   # recebe 0.0.0.0:80
        udp_banner=""
        udp_pcount=0
        if p_udp_l is not "" and p_udp_l is not None:   # Se realmente recebeu uma tupla de porta aberta
            for svcudp in p_udp_l.split(','):           # entao vamos tokenizar cada tupla separada por virgula (se tiver mais de1 porta aberta por processo)
                try:
                    ip=svcudp.split(':')[0]
                    porta=svcudp.split(':')[1]
                    p_udp_fp_l={}
                    p_udp_fp_l = item.getDaemonUdpFp()
                    fp_item=p_udp_fp_l.get(int(porta))
                    #print "ip: " + ip + " porta: " + porta + " banner: " + fp_item 
                    if Dry==True:
                         print "PROCESS UDP FINGERPRINT: " +str(porta)+":"+str(fp_item)
                    udp_banner=porta+":"+b64encode(fp_item) # porta:banner em base64 
                    udp_pcount+=1
                    
                except:
                    continue
        

        if Dry==True:
            print "*"*100
            continue

        if PingManager(manageraddr)==1:
            sent_count+=1
            SendData(manageraddr,server,domain,GetLinuxDist(DIST_NAME),GetLinuxDist(DIST_VER),p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args,tcp_banner,udp_banner)
        else:
            print "[x] Manager offline"

        print "[+] Sent: %d itens" %sent_count

    return 0
        

def main():
    print "v-gather CBR"
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:tdh")
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
        if opcao == "-d":
            StartScan(True,argumento)
        if opcao == "-h":
            usage()
        if opcao == "-a":
            StartScan(False,argumento)
        


if __name__ == "__main__":
    main()









