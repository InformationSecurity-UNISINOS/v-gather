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

''' Esta funcao retorna tipo do arquivo
'   tipo pode ser, socket, arquivo regular, device, link, diretorio, etc
'''
def GetFileType(filestr):
    try:
        mode = os.stat(filestr).st_mode
    except:
        return -1

    if stat.S_ISDIR(mode):
        return FT_DIR
    if stat.S_ISCHR(mode):
        return FT_CHR
    if stat.S_ISBLK(mode):
        return FT_BLK
    if stat.S_ISREG(mode):
        return FT_REG
    if stat.S_ISFIFO(mode):
        return FT_FIF
    if stat.S_ISLNK(mode):
         return FT_LNK
    if stat.S_ISSOCK(mode):
        return FT_SCK



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

''' Esta funcao retorna as informacoes do usuario
'   disponiveis no arquivo /etc/passwd
'''
def GetUserInfo(uid):
    
    try:
        userinfo=[]
        userinfo.append(pwd.getpwuid(int(uid)).pw_name)
        userinfo.append(pwd.getpwuid(int(uid)).pw_uid)
        userinfo.append(pwd.getpwuid(int(uid)).pw_gid)
        userinfo.append(pwd.getpwuid(int(uid)).pw_dir)
        userinfo.append(pwd.getpwuid(int(uid)).pw_shell)
        return userinfo
    except:
        return -1
'''
' Verifica qual é o processador presente
' e quantos cores tem
'''
def CheckProcessor():
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    print(model_name)

'''
' Função recursiva de visita a diretórios
' pode ser usado para localizar arquivos
' ou permissões específicas
'
' DACSEARCH: procura por arquivos que estejam sob
'            determinado esquema de permissoes
' DIRSEARCH: procura por determinado nome de diretório
' FILESEARCH: procura por determinado nome de arquivo
' FTYPESEARCH: procura por um tipo determinado de arquivo (devices, sockets, etc)
'
'''
def WalkDir(dirstr, searchstr, mode):

    
    if mode == DACSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            for fname in fileList:
                fullpath=dirName+"/"+fname
                if not re.search('^/proc/.+', fullpath):
                    if CheckDacMode(fullpath,searchstr,False) == True:
                        filesfound.append(fullpath)
    
    if mode == DIRSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            if searchstr in dirName:
                    filesfound.append(dirName)

    if mode == FILESEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            for fname in fileList:
                if searchstr in fname:
                    fullpath=dirName+"/"+fname
                    filesfound.append(fullpath)

    if mode == FYPESEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            for fname in fileList:
                fullpath=dirName+"/"+fname
                if not re.search('^/proc/.+', fullpath):
                    if GetFileType(fullpath) == searchstr:
                        filesfound.append(fullpath)

    
    return filesfound

'''
' Procura por arquivos ou diretórios com permissao de escrita
' para  
'''
def SearchWritable(dirstr, uid,gid, mode):
    filesfound=[]
    if mode == WDIRSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            fullpath=dirName
            if not re.search('^/proc/.+', fullpath):
                if GetFileType(fullpath) != FT_LNK:
                    if CheckWrite(fullpath,uid,gid) == True:
                        filesfound.append(fullpath)

    if mode == WFILSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            for fname in fileList:
                fullpath=dirName+"/"+fname
                if not re.search('^/proc/.+', fullpath):
                    if GetFileType(fullpath) != FT_LNK:
                        if CheckWrite(fullpath,uid,gid) == True:
                            filesfound.append(fullpath)
    return filesfound
'''
' Procura por arquivos ou diretórios com permissao de leitura
' para determinado uid e/ou gid
'''
def SearchReadable(dirstr, uid,gid, mode):
    filesfound=[]
    if mode == RDIRSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            fullpath=dirName
            if not re.search('^/proc/.+', fullpath):
                if GetFileType(fullpath) != FT_LNK:
                    if CheckWrite(fullpath,uid,gid) == True:
                        filesfound.append(fullpath)

    if mode == RFILSEARCH:
        filesfound=[]
        for dirName, subdirList, fileList in os.walk(dirstr):
            for fname in fileList:
                fullpath=dirName+"/"+fname
                if not re.search('^/proc/.+', fullpath):
                    if GetFileType(fullpath) != FT_LNK:
                        if CheckWrite(fullpath,uid,gid) == True:
                            filesfound.append(fullpath)
    return filesfound
'''
' Verifica se determinado usuario pode escrever no arquivo
'''
def CheckWrite(file,uid,gid):
    try:
        st = os.stat(file)
    except:
        return -1
    uid=int(uid)
    gid=int(gid)
    ouid = int(st.st_uid)
    ogid = int(st.st_gid)
    mode = st.st_mode
    writable=False
    
    if uid == ouid and (stat.S_IWUSR & mode):
        writable=True
    if gid == ogid and (stat.S_IWGRP & mode):
        writable=True
    if uid != ouid and (stat.S_IWOTH & mode):
        writable=True
    if gid != ogid and (stat.S_IWOTH & mode):
        writable=True

    return writable


'''
' Verifica se determinado usuario pode ler arquivo
'''
def CheckRead(file,uid,gid):
    try:
        mode = os.stat(filepath).st_mode
    except:
        return -1
    uid=int(uid)
    gid=int(gid)
    ouid = int(st.st_uid)
    ogid = int(st.st_gid)
    readable=False

    if uid == ouid and (stat.S_IRUSR & mode):
        readable=True
    if gid == ogid and (stat.S_IRGRP & mode):
        readable=True
    if uid != ouid and (stat.S_IROTH & mode):
        readable=True
    if gid != ogid and (stat.S_IROTH & mode):
        readable=True
    return readable

'''
' Verifica se determinado usuario pode executar arquivo
'''
def CheckExec(file,uid,gid):
    try:
        st = os.stat(file)
    except:
        return -1
    uid=int(uid)
    gid=int(gid)
    ouid = int(st.st_uid)
    ogid = int(st.st_gid)
    mode = st.st_mode
    executable=False
    
    if uid == ouid and (st.S_IXUSR & mode):
        executable=True
    if gid == ogid and (st.S_IXGRP & mode):
        executable=True
    if uid != ouid and (st.S_IXOTH & mode):
        executable=True
    if gid != ogid and (st.S_IXOTH & mode):
        executable=True
    return executable

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


def GetFileMagicStr(fullpath):
    import magic
    try:
        ft = magic.from_file(fullpath)
    except:
        ft = None
    return ft
    
    
'''
'' Recebe lista de arquivos e retorna uma nova lista contendo
'' uma lista da classe fileinfo
''
'''
def GetFileProperties(filelist):

    ret=[]
    for token in iter(filelist):
        finfo=FileInfo()
        finfo.dac=mfs.GetDacMode(token)
        finfo.file=token
        
        owner=GetOwnerName(token)
        if owner[0]>0:
            finfo.uname=str(owner[0])
        if owner[1]>0:
            finfo.gname=str(owner[1])
        finfo.type=GetFileMagicStr(token)
        
        owner=CheckIdOwner(token)
        finfo.uid=int(owner[0])
        finfo.gid=int(owner[1])
        
        if GetFileType(filelist) == FT_LNK:
            finfo.link=True
        
        if GetFileType(filelist) == FT_DIR:
            finfo.dir=True
        
        if GetFileType(filelist) == FT_CHR:
            finfo.chr=True
        
        if GetFileType(filelist) == FT_BLK:
            finfo.blk=True
        
        if GetFileType(filelist) == FT_REG:
            finfo.reg=True
        
        if GetFileType(filelist) == FT_FIF:
            finfo.fif=True
        
        if GetFileType(filelist) == FT_SCK:
            finfo.sck=True

        ret.append(finfo)
    return ret

    
    
    
    
    
    
