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
from rbase import *
import getopt

def usage():
    print "%s <opcao> "
    print "\t-s\tMostrar estado da base de casos"
    print "\t-a\tAnalisar ambiente"
    print "\t-r\tRegistrar um novo caso (interativo)"
    print "\t-c arquivo.txt\tCarregar novo caso a partir de um arquivo"
    print "\t-e arquivo.txt\tExportar base de casos para texto plano"


def StartScan():
    GetDaemons()
    DumpBase(nlist)
    nlist=[]
    nlist=OpenBase()
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

def ShowDBStatus():
    print "status beleza"
    print "existem x casos na base"

def RegisterCase():
    print "beleza, vamos registrar"

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









