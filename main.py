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


# pega argumentos da linha de comando:
# -c verificar configuraçoes de serviços apenas
# -d verificar esquema DAC de arquivos apenas
# -a verificar tudo
# -i realizar apenas o fingerprint deste sistema e reportar quantos casos existem na base
# -w salvar resultado em arquivo texto
# -f formato do arquivo report (txt ou xml)
# -v modo verbose (apenas 1 nivel)
# -x explorar automaticamente alguma vulnerabilidade que permita escalada de privilégios para o uid a ser especificado via switch -t
# -t especifica qual é o uid alvo da exploração (escalada de privilégios)



#CheckLinuxDist("Kali","1.0.7",True)

#CheckDacMode("/tmp/teste",04755,True)
#

#owner=GetOwnerName("/tmp/teste",True)
#if owner[0]>0:
#    print "User: "+ str(owner[0]) + " Group: " + str(owner[1])
#    owner=CheckIdOwner("/tmp/teste",True)
#    print "uid: "+ str(owner[0]) + " guid: " + str(owner[1])
#    print GetUserInfo(owner[0],True)

#print "Porcurando pelo arquivo suidt:"
#files=WalkDir("/", "suidt", FILESEARCH)
#print "Arquivos encontrados: " + str(len(files))
#for arquivo in files:
#    print "Arquivo: " + str(arquivo)


#print "*"*100
#print "Porcurando por arquivos suid:"
#files=WalkDir("/", 04755, DACSEARCH)
#print "Arquivos encontrados: " + str(len(files))
#for arquivo in files:
#    owner=GetOwnerName(arquivo,True)
#    nowner=CheckIdOwner(arquivo,True)
#    print str(nowner[0]) +"/"+ str(owner[0]) + " \t " + str(nowner[1]) +"/" +str(owner[1]) + " \t " + str(arquivo)
#CheckProc()
#
#print "Porcurando por arquivos socket:"
#files=WalkDir("/", FT_SCK, FYPESEARCH)
#print "Arquivos encontrados: " + str(len(files))
#for arquivo in files:
#    owner=GetOwnerName(arquivo,False)
#    nowner=CheckIdOwner(arquivo,False)
#    print str(nowner[0]) +"/"+ str(owner[0]) + " \t " + str(nowner[1]) +"/" +str(owner[1]) + " \t " + str(arquivo)
#print "*"*100
#print "Porcurando pelo diretorio cron:"
#files=WalkDir("/var/spool", "cron", DIRSEARCH)
#print "Arquivos encontrados: " + str(len(files))
#for arquivo in files:
#    owner=GetOwnerName(arquivo,False)
#    nowner=CheckIdOwner(arquivo,False)
#    print str(nowner[0]) +"/"+ str(owner[0]) + " \t " + str(nowner[1]) +"/" +str(owner[1]) + " \t " + str(arquivo)


#print "*"*100
#files=SearchWritable("/", 501,501, WFILSEARCH)
#print "Arquivos que o usuario 501 pode escrever: " + str(len(files))
#for arquivo in files:
#    owner=GetOwnerName(arquivo,False)
#    nowner=CheckIdOwner(arquivo,False)
#    print str(nowner[0]) +"/"+ str(owner[0]) + " \t " + str(nowner[1]) +"/" +str(owner[1]) + " \t " + str(arquivo)
#print "*"*100
#verifica se tem algum processo do mysql rodando, se tiver, retorna a linha visivel no ps aux
#p=CheckRunningProc("mysql",False)
#if p: 
#    for cmd in p:
#        print cmd


#print GetLinuxDist()
#print "*"*100
#if GetLinuxDist().lower()=="debian":
#    pacote=CheckDpkg("sudo","1.8.5p2-1+nmu1")

#if GetLinuxDist().lower()=="centos":
#    pacote=CheckRpm("sudo","1.8.6p3")
#if pacote==PKG_FOUND:
#    print "Instalado"
#if pacote==PKG_VERMATCH:
#    print "Versão confere!!!"
#if pacote==PKG_NOTFOUND:
#    print "Não instalado!"

#print "*" * 500
#print "VERIFICANDO ARQUIVOS ABERTOS"
#CheckProOpencFiles()

#pacote=FileToPackage("/usr/bin/id")
#print pacote

GetDaemons()
DumpBase(nlist)
nlist=[]
nlist=OpenBase()

for item in nlist:
        print "Daemon: %s"  %item.getDaemon()
        print "Pid: %d"  %item.getDaemonPid()
        print "Daemon Uid: %d" %item.getDaemonUid()
        print "Daemon Gid: %d" %item.getDaemonGid()
        
        print "Daemon IO Files: %s" %item.getDaemonIo()
        
        
        
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
        print "*"* 150#


















