#!/usr/bin/python

import socket
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
servername = sys.argv[1]
server_address = (servername, 81)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = 'GET /filename.html HTTP/1.1'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
    data = sock.recv(1024)
    print >>sys.stderr, 'received first 1024 chars from server:\n%s\n-----(client program note: End of file!)-----' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
