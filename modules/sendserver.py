import socket
import sys
import common

def SendData(data):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((MANAGER, PORTA))
    sock.sendall(data + "\n")
    #received = sock.recv(1024)
finally:
    sock.close()

#print "Sent:     {}".format(data)
#print "Received: {}".format(received)
