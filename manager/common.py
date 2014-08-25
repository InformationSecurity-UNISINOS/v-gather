# -*- coding: utf-8 -*-
'''
' DEFINICOES GLOBAIS 
'''
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

#DEFINICOES DE SERVICO
BUFSIZE=200000
PORTA=3339
BINDIP="0.0.0.0"

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

def CheckMatch(pattern,string):
 import re
 if re.match(pattern,string):
    return True
 else:
    return False


def HandleStream(stream):
    import pickle
    import pickletools

    y=[]
    y = pickle.load(stream)
    return y

from twisted.web import xmlrpc, server
class XmlHandler(xmlrpc.XMLRPC):
    def xmlrpc_ping(self):
        return True

    def xmlrpc_echo(self,item):
        print item
        return True
    
    def xmlrpc_banner(self,payload):
        print "banner"
        return True
    
    def xmlrpc_args(self,payload):
        print "args"
        return True
    
    def xmlrpc_general(self,payload):
        print "general"
        return True
    
    def xmlrpc_ofiles(self,payload):
        print "ofiles"
        return True
    
    
    

    def xmlrpc_Fault(self):
        """
        Raise a Fault indicating that the procedure should not be used.
        """
        raise xmlrpc.Fault(123, "The fault procedure is faulty.")











