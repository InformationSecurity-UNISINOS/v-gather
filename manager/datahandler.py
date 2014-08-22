#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import *

def Deserialize(serialized):
    import pickle
    import pickletools
    return pickle.loads(serialized)
 
def HandleStream(stream):
    data=Deserialize(stream)
    ProcessData(data)

def ProcessData(data):
    nlist=[]
    nlist=data
    for item in nlist:
        print "Daemon: %s"  %item.getDaemon()
        print "Pid: %d"  %item.getDaemonPid()
        print "Daemon Uid: %d" %item.getDaemonUid()
        print "Daemon Gid: %d" %item.getDaemonGid()
        print "Daemon IO Files:"
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
            print "\t%s\t%s\t%d\t%s" %(user,group,token.getDac(),token.getFile())
            
        print "Daemon Args: %s" %item.getDaemonArgs()

        print "Daemon TCP port: %s" %item.getDaemonTcp()
        print "Daemon TCP FP: %s" %item.getDaemonTcpFp()

        print "Daemon UDP port: %s" %item.getDaemonUdp()
        print "Daemon UDP FP: %s" %item.getDaemonUdpFp()
        print "Daemon file Path: %s" %item.getFilePath()
        print "Daemon Rpm Package: %s" %item.getDaemonRpm()
        print "Daemon Dpkb Package: %s" %item.getDaemonDpkg()
        print "Daemon File Dac: %d" %item.getFileDac()
        print "Daemon File Uid: %d" %item.getFileUid()
        print "Daemon File Gid: %d" %item.getFileGid()
        print "*"* 150
