import socket
import sys
import CommandParser
import CommandMaker
import treading

def openServerThread(serverHandler):
	serverThread = threading.Thread(target= serverCatchPackets, args=(serverHandler,))
	return serverThread

def serverCatchPackets(serverHandler):
	if Server.startListening() == 1: #Start Listening
		try:
			while True:
				Commands = CommandParser.getCommand(serverHandler)
				CommandMaker.controlCommands(Commands)	#doCommands
		except Exception:
			return -1

class qcServer:

	def __init__(self, port):
		self.port = port 
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Setting the socket . 
		self.serverSocket.bind((socket.gethostname(), port)) # Setting the socket as Server .
		self.serverSocket.listen(1) # Listening to only 1 connection .


	def startListening(self): # Accepting client connection .
		print 'Listening ...'
		self.conn, addr = self.serverSocket.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])
		return 1


	def getPackets(self): # Start recieving packets from the client
		data = self.conn.recv(1024)
		return data


	def closeServer(self): # Closing .. 
		self.serverSocket.close()
		print 'Server is Closed.'