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
        if PingManager()==1:
            SendData(server,domain,p_pid,p_name,p_uid,p_gid,p_rpm,p_dpkg,pf_path,pf_dac,pf_uid,pf_gid,p_args)
        else:
            print "[x] Manager offline"
        #p_tcp_l = item.getDaemonTcp()
        #tbuf=None
        #for svctcp in p_tcp_l.split(','):
        #    try:
        #        ip = svctcp.split(':')[0]
        #        porta = svctcp.split(':')[1]
        #        p_tcp_fp_l={}
        #        p_tcp_fp_l = item.getDaemonTcpFp()
        #        fp_item=p_tcp_fp_l.get(int(porta))
        #        if fp_item is not '' and fp_item is not None:
        #            banner=b64encode(fp_item)
        #            tbuf="tcp:"+ip+":"+porta+":"+banner
        #            break
        #            
        #    except:
        #        continue

        #p_udp_l = item.getDaemonUdp()
        #ubuf=None
        #for svcudp in p_udp_l.split(','):
        #    try:
        #        ip = svcudp.split(':')[0]
        #        porta = svcudp.split(':')[1]
        #        p_tcp_fp_l={}
        #        p_udp_fp_l = item.getDaemonUdpFp()
        #        fp_item=p_udp_fp_l.get(int(porta))
        #        if fp_item is not '' and fp_item is not None:
        #            banner = b64encode(fp_item)
        #            ubuf="udp:"+ip+":"+porta+":"+banner
        #            break
        #            #SendData(BANNER,server,domain,p_pid,buf)
        #    except:
        #        continue

        #if tbuf is not None:
        #    #banner=tbuf
        #    SendBanner(server,domain,p_pid,tbuf)
        #if ubuf is not None:
        #    SendData(BANNER,server,domain,p_pid,ubuf)
        #    #banner=ubuf

        #iof=item.getDaemonIo()
        #for token in iter(iof):
        #    if token.getUname() == None:
        #        user=token.getUid()
        #    else:
        #        user=token.getUname()

        #   if token.getGname() == None:
        #        group=token.getGid()
        #    else:
        #        group=token.getGname()
        #    
        #    buf = str(user)+":"+str(group)+":"+str(token.getDac())+":"+token.getFile()
        #    pf_io = str(p_pid)+":"+b64encode(buf)
        #    SendOfiles(server,domain,p_pid,pf_io)

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









