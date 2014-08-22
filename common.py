# -*- coding: utf-8 -*-
'''
' DEFINICOES GLOBAIS 
'''

#COMUNICACAO COM O MANAGER
PORTA=3339
MANAGERADDR="10.211.55.12"

# Tipos de pesquisa, usados na funcao WalkDir
DACSEARCH=1
DIRSEARCH=2
FILESEARCH=3
FYPESEARCH=4
WDIRSEARCH=5
WFILSEARCH=6
RDIRSEARCH=7
RFILSEARCH=8
#definição de opt para função GetLinuxDist
DIST_NAME=20
DIST_VER=21

# Tipos de arquivos
FT_SCK=100 # socket
FT_DIR=101 # diretorio
FT_REG=102 # arquivo regular
FT_LNK=103 # link
FT_BLK=104 # bloco
FT_CHR=105 # dispositivo de caracteres
FT_FIF=106 # FIFO

# Constantes sobre pacotes (usados em mfs.py)
PKG_NOTFOUND=404
PKG_FOUND=204
PKG_VERMATCH=200

class DaemonInfo(object):
        def __init__(self):
                self.daemon = None
                self.pid = None
                self.downer_uid = None
                self.downer_gid = None
                self.io_files=[]
                self.args = None
                self.tcp = []
                self.svc_tcp_fp = {}
                self.udp = []
                self.svc_udp_fp = {}
                self.dpkg = None
                self.rpm = None
                self.file_path = None
                self.file_dac = None
                self.file_uid = None
                self.file_gid = None
        def getDaemon(self):
                return self.daemon
        def getDaemonPid(self):
                return self.pid
        def getDaemonUid(self):
                return self.downer_uid
        def getDaemonGid(self):
                return self.downer_gid
        def getDaemonIo(self):
                return self.io_files
        
        def getDaemonArgs(self):
                return self.args
        def getDaemonTcp(self):
                return self.tcp
        def getDaemonUdp(self):
                return self.udp
        def getDaemonUdpFp(self):
                return self.svc_udp_fp
        def getDaemonTcpFp(self):
                return self.svc_tcp_fp
        def getDaemonDpkg(self):
                return self.dpkg
        def getDaemonRpm(self):
                return self.rpm
        def getFilePath(self):
                return self.file_path
        def getFileDac(self):
                return self.file_dac
        def getFileUid(self):
                return self.file_uid
        def getFileGid(self):
                return self.file_gid

        def __str__(self):
                return "%s %s" % (self.daemon, self.args)


class FileInfo(object):
        def __init__(self):
                self.file = None
                self.uid = None
                self.gid = None
                self.uname = None
                self.gname = None
                self.type = None
                self.dac = None
                self.link = None
                self.dir = None
                self.chr = None
                self.blk = None
                self.reg = None
                self.fif = None
                self.sck = None
        def getFile(self):
                return self.file
        def getUid(self):
                return self.uid
        def getGid(self):
                return self.gid
        def getUname(self):
                return self.uname
        def getGname(self):
                return self.gname
        def getType(self):
                return self.type
        def getDac(self):
                return self.dac
        def isLink(self):
                return self.link
        def isDir(self):
                return self.dir
        def isChr(self):
                return self.chr
        def isBlk(self):
                return self.blk
        def isReg(self):
                return self.reg
        def isFif(self):
                return self.fif
        def isSck(self):
                return self.sck

        def __str__(self):
                return "%s %s %s" % (self.uname, self.gname, self.file)



nlist=[]
#portas ja scaneadas: 
svc_udp_checked={}
svc_tcp_checked={}

def CheckMatch(pattern,string):
 import re
 if re.match(pattern,string):
    return True
 else:
    return False


def CheckIpv4(ipaddr):
    import re
    pattern4="[^:]\b([0-1]?\d{1,2}|2[0-4]\d|25[0-5])(\.([0-1]?\d{1,2}|2[0-4]\d|25[0-5])){3}"
    if re.match(pattern4,ipaddr):
        return(True)
    else:
        return(False)

def CheckIpv6(ipaddr):
    import re
    pattern6="([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:"
    if re.match(pattern6,ipaddr):
        return(True)
    else:
        return(False)





