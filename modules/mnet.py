# -*- coding: utf-8 -*-
import common
import nmap
'''
''verifica fingerprint do servico que atende
'' determinada porta 
'''
def CheckSvcFPrint(ip,port,proto):
    nm=nmap.PortScanner()
    fprint=""
    if ip == '0.0.0.0':
        ip="127.0.0.1"
    if proto == "UDP":
        args="-n -sUV -T5 --version-intensity 0 -p "+str(port)
        nm.scan(ip,arguments=args)
        nmres = nm[ip]['udp'][port]
        fprint = nmres['product']

    if proto == "TCP":
        args="-n -sSV -T5 -p " + str(port)
        nm.scan(ip,arguments=args)
        nmres = nm[ip]['tcp'][port]
        fprint = nmres['product']

    #print "PORTA: %s" %str(port)
    return fprint