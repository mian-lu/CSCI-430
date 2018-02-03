print "hello world!"

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('server', 81)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()

	try:
		print >>sys.stderr, 'connection from', client_address

		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(1024)
			print >>sys.stderr, 'received "%s"' % data
			if data:
				filename = (data.split(" "))[1]
				print "trying to open /tmp"+filename+" and see if fails..."
				try:
					file = open("/tmp"+filename, "r")
					print >> sys.stderr, 'read success! sending data back to the client'
					connection.sendall(file.read())
				except IOError:
					print("read file failed! sending error message to client!")
					connection.sendall("cannot open \"%s\"! please check file path before sending!" % filename)
			else:
				print >>sys.stderr, 'no more data from', client_address
				break

	finally:
		# Clean up the connection
		connection.close()
