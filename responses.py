import responsesExt

##########################################################
def handle_response(message, username, usernameID) -> str:
    #This makes sure that any command in any form of caps is met
    p_message = message.lower()
    
    #Create dictionary of commands
    commands = {"-help":0, "-h":0, "h":0, "help":0, "-steamid":0, "-leaders":0, "-top":0, "-givetop":0, "-avg":0, "-bottom":0, "-condone":0, "-bestgame":0, "-worstgame":0, "-lastgame":0, "-pos":0}
    commands["-sum"] = 0
    commands["-summary"] = 0
    try:
        command = p_message.split(" ")[0]
    except:
        command = None
    
    #Instead of checking every command end it here
    if command not in commands:
        return
    
    #Display help message to the user
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        return responsesExt.help()
    
    #This allows a user to see their position on the leaderboards
    if command == "-pos":
        return responsesExt.pos(username, p_message, usernameID)
    
    #This allows the user to see their last game
    if command == "-lastgame":
        return responsesExt.lastgame(username, p_message, usernameID)
    
    #This allows a user to find their best game
    if command == "-bestgame":
        return responsesExt.bestgame(username, p_message, usernameID)
    
    #this allows a user to find their worst game
    if command == "-worstgame":
        return responsesExt.worstgame(username, p_message, usernameID)
    
    #Returns the top x (between 0 and 100) for all users in database of a given category
    if command == "-leaders":
        return responsesExt.leaders(p_message)
    
    #Returns the top x (between 0 and 100) for the user creating the command of a given category
    if command == "-top" or command == "-givetop":
        return responsesExt.top(usernameID, p_message, username)
    
    #Gives the user their average
    if command == "-avg":
        return responsesExt.avg(usernameID, p_message, username)
    
    #Gives the user their sum
    if command == "-sum":
        return responsesExt.sum(usernameID, p_message, username)
    
    #Gives the user bottom of a category
    if command == "-bottom":
        return responsesExt.bottom(p_message) 
    
    #Gives a summary for the users in the last game
    if command == "-summary":
        return responsesExt.summary()
    
    #Condone
    if command == "-condone":
        return "5 big guys does not condone: valorant, will flashes, wes holding outside, office, men"
    
    #Testing buttons
    if command == "-menu":
        return 
       
    return

