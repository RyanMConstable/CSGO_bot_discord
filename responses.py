from CSGO_Project import CSGOsql, findMatchSteamAPI, getJSONInfo

##########################################################
def handle_response(message, username, usernameID) -> str:
    p_message = message.lower()
    try:
        command = p_message.split(" ")[0].lower()
    except:
        command = None

    #Display help messages
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        returnString = "Commands:\n  -steamid <id> <steamkey>\n  -top <amount> <category>\n  -topuser10 <category>\n    Categories: [totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown, molly_thrown, incendiary_thrown, decoy_thrown, round_count]" 
        return returnString 
    
    
    
    #This allows a user to add their steamid to the database for future reference
    if command == "-steamid":
        try:
            CSGO_Project.CSGOsql.setDiscordUser(usernameID, p_message.split(" ")[1], message.split(" ")[2].upper())
        except:
            return "Incorrect Input try '-steamid <id> <key>'"
        return "SteamID updated"
    
    
    
    #Easy commands to find stats for
    if command == "-top":
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGO_Project.CSGOsql.findTopX(category, num)
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Incorrect format, try '-top <amount> <category>'"
    
    #This command makes the discord bot time out because it takes so long... Find a way to do this asynchronously?
    if command == "-update":
        try: 
            CSGO_Project.CSGOsql.updateAllUsers()
        except:
            return "Failure"
        return "Updated all users"
    
    
    
    
    
    
    #Specific user commands
    if command == "-topuser10":
        id = CSGO_Project.CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid <id>'"
        category = p_message.split(" ")[1]
        return CSGO_Project.CSGOsql.findTop10user(category, id[0])
            
    if command == "-updategames":
        id = CSGO_Project.CSGOsql.findSteamID(usernameID)
        if id is None or id == []:
            return "Can't find an id linked with your discord? Use '-steamid <id>'"
        CSGO_Project.CSGOsql.updateGames(id[0], id[1])
        return "Updating games"
    
    
    return

