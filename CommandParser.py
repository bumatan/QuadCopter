import Server
import json

def getCommands(Server): #Parses the commands and puts it in a dictionary
	Data = Server.getPackets()
	commands_in_dict = json.loads(Data)
	return commands_in_dict