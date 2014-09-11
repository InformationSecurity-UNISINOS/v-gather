# -*- coding: utf-8 -*-
'''
'' Requerimentos: psutil
''
'' 
''
''
''
'''

import os
import sys
import stat
import pwd, grp
import re
from common import *
from mvram import *


''' Esta função verifica se o pacote informado está instalado
'   e se a versão confere
'''

def GetRpmDict():
    import rpm
    ts = rpm.TransactionSet()
    rpmlist = ts.dbMatch()
    rdb={}
    for pkg in rpmlist:
        rdb[pkg['name']]=pkg['version']
    return rdb

def CheckRpm(package):
    rpmdb=GetRpmDict()
    ret=PKG_NOTFOUND
    if rpmdb.has_key(package)==True:
        ret=PKG_FOUND
        if rpmdb.get(package)==version:
                ret=PKG_VERMATCH
    return ret

def CheckDpkg(package):
    dpkgdb=GetDpkgDict()
    ret=PKG_NOTFOUND
    if dpkgdb.has_key(package)==True:
        ret=PKG_FOUND
        if dpkgdb.get(package)==version:
            ret=PKG_VERMATCH

    return ret

'''
'' Retorna a versão de um dpkg
'''
def GetDpkgVer(package):
    dpkgdb=GetDpkgDict()
    if dpkgdb.has_key(package)==True:
        return dpkgdb.get(package)

def GetDpkgDict():
    dpkg_all=[]
    fpkg=0
    pdb={}
    file = open('/var/lib/dpkg/status', 'r')
    pattern="(Package:.+|Status:.+|^(Version:).+)"
    for line in file:
        match=re.findall(pattern,line)
        for m in match:
            dpkg_all.append(m[0])
            dpkg_len=len(dpkg_all)
            for i in xrange(0,dpkg_len-1,3):
                if dpkg_all[i+1] == "Status: install ok installed":
                    try:
                        dkey=dpkg_all[i].split(' ')[1]
                        dval=dpkg_all[i+2].split(' ')[1]
                        pdb[dkey]=dval
                    except:
                        continue
    return pdb




''' Esta função verifica se o esquema de permissões DAC
'   é igual ao informado por parametro
'''
def CheckDacMode(filestr,dacstr,verbose):
    
    try:
        dacmode =  oct(os.stat(filestr).st_mode & 07777)
    except:
        dacmode = -1
    
    dacstr = int(oct(dacstr))
    dacmode=int(dacmode)

    if dacmode == dacstr:
        if verbose == True:
            print "<+> Esquema DAC é igual"

        return True
    else:
        return False

'''
'' Recupera o DAC do arquivo
''
'''
def GetDacMode(filestr):
    
    try:
        dacmode =  oct(os.stat(filestr).st_mode & 07777)
    except:
        dacmode = -1
    dacmode=int(dacmode)

    return dacmode



def CheckIdOwner(filestr):
    owner={}
    try:
        st = os.stat(filestr)
        owner[0]=st.st_uid
        owner[1]=st.st_gid
    except:
        owner[0]=owner[1]=-1
    
    return owner

''' Esta funcao retorna o nome do usuario dono do arquivo
'   e o grupo do dono também
'   retorna um array contendo nos campos
'   0 = user owner
'   1 = group owner
'''
def GetOwnerName(filestr):
    owner={}
    try:
        st = os.stat(filestr)
        owner[0]=pwd.getpwuid(st.st_uid).pw_name
        owner[1]=grp.getgrgid(st.st_gid).gr_name
    except:
        owner[0]=owner[1]=-1
    return owner


'''
'' Qual pacote instalado fornece tal arquivo
'''
def FileToDpkg(searchstr):
    if not GetLinuxDist(DIST_NAME).lower()=="debian":
        return None
    else:
        dpkg_list="/var/lib/dpkg/info/"
        for dirName, subdirList, fileList in os.walk(dpkg_list):
                for fname in fileList:
                        fullpath=dirName+"/"+fname
                        if ".list" in fullpath:
                                with open(fullpath) as f:
                                        for line in f:
                                                pattern="^" + searchstr + "$"
                                                if re.search(pattern,line):
                                                        pname=os.path.basename(fullpath).split('.')[0]
                                                        pver=GetDpkgVer(pname)
                                                        if pver != None:
                                                            package=pname+"-"+pver
                                                        else:
                                                            package=pname
                                                        return package

def FileToRpm(searchstr):
    import rpm
    package=""
    ts = rpm.TransactionSet()
    headers = ts.dbMatch('basenames', searchstr)
    for h in headers:
        package = h['name'] + "-" + h['version']
    return package


def FileToPackage(searchstr):
    if GetLinuxDist(DIST_NAME).lower()=="debian":
        ret=FileToDpkg(searchstr)
    if GetLinuxDist(DIST_NAME).lower()=="centos":
        ret=FileToRpm(searchstr)
    return ret

    
