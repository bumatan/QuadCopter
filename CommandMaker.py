import Controls

def controlCommands(CommandsDict):
	CommandsList = [command1, command2, command3] #The command list, here is the keys for the commands.
	for Command in CommandsList:
		if Command in CommandsDict.keys():
			callCommand(Command, Value)

def callCommand(Command, Value): #Calls the right command
	if Command = Forward:
		FlyForward(Value)
	else if 