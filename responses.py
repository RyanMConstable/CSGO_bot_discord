import responsesExt

##########################################################
def handle_response(message, username, usernameID) -> str:
    #This makes sure that any command in any form of caps is met
    p_message = message.lower()
    
    #Create dictionary of commands
    commands = {"-help": 0, "-h": 0, "h": 0, "help":0, "-steamid":0, "-leaders":0, "-top":0, "-givetop":0, "-avg":0, "-bottom":0}
    try:
        command = p_message.split(" ")[0].lower()
    except:
        command = None
    
    #Instead of checking every command end it here
    if command not in commands:
        return
    
    #Display help message to the user
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        return responsesExt.help()
    
    #This allows a user to add their steamid to the database for future reference
    if command == "-steamid":
        return responsesExt.steamid(usernameID, p_message.split(" ")[1], message.split(" ")[2].upper())
    
    #Returns the top x (between 0 and 100) for all users in database of a given category
    if command == "-leaders":
        return responsesExt.leaders(p_message)
    
    #Returns the top x (between 0 and 100) for the user creating the command of a given category
    if command == "-top" or command == "-givetop":
        return responsesExt.top(usernameID, p_message, username)
    
    #Gives the user their average
    if command == "-avg":
        return responsesExt.avg(usernameID, p_message, username)
    
    #Gives the user bottom of a category
    if command == "-bottom":
        return responsesExt.bottom(message) 
       
    return

