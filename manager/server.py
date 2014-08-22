#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(BUFSIZE).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

def StartServer():
    server = SocketServer.TCPServer((BINDIP, PORTA), MyTCPHandler)
    server.serve_forever()