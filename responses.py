from CSGO_Project import CSGOsql

##########################################################
def handle_response(message, username, usernameID) -> str:
    p_message = message.lower()
    try:
        command = p_message.split(" ")[0].lower()
    except:
        command = None

    #Display help messages
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        returnString = "Commands:\n  -steamid <id> <steamkey>\n  -myavg\n  -top <amount> <category>\n  -topuser <amount> <category>\n    Categories: [totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown, molly_thrown, incendiary_thrown, decoy_thrown, round_count]" 
        return returnString 
    
    
    
    #This allows a user to add their steamid to the database for future reference
    if command == "-steamid":
        #Here we should attempt an API call to validate the user...
        try:
            CSGOsql.setDiscordUser(usernameID, p_message.split(" ")[1], message.split(" ")[2].upper())
        except:
            return "Incorrect Input try '-steamid <id> <key>'"
        return "SteamID updated"
    
    
    
    #Easy commands to find stats for
    if command == "-top":
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGOsql.findTopX(category, num)
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Incorrect format, try '-top <amount> <category>'"
    
    
    
    
    
    #Specific user commands
    if command == "-topuser":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGOsql.findTop10user(category, id[0], num)
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Incorrect format, try '-topuser <amount> <category>'"
    
    
    if command == "-myavg":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        try:
            strVal = "Average stats per game:\n"
            
            strVal += "\nTotal Games: " + str(CSGOsql.findNumberOfGames(id[0]))
            strVal += "\nKills: " + str(CSGOsql.selectAvgUserStat("totalkills", id[0]))
            strVal += "\nScore: " + str(CSGOsql.selectAvgUserStat("score", id[0]))
            strVal += "\nTeam Kills: " + str(CSGOsql.selectAvgUserStat("tk_count", id[0]))
            strVal += "\nAssists: " + str(CSGOsql.selectAvgUserStat("assist", id[0]))
            strVal += "\nDeaths: " + str(CSGOsql.selectAvgUserStat("deaths", id[0]))
            strVal += "\nHeadshots: " + str(CSGOsql.selectAvgUserStat("headshot", id[0]))
            strVal += "\nKD: " + str(CSGOsql.selectAvgUserStat("kd", id[0]))
            strVal += "\nRWS: " + str(CSGOsql.selectAvgUserStat("rws", id[0]))
            strVal += "\nShot Count: " + str(CSGOsql.selectAvgUserStat("shot_count", id[0]))
            strVal += "\nHit Count: " + str(CSGOsql.selectAvgUserStat("hit_count", id[0]))
            return strVal
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Error, most likely invalid steamid/steam key"
        
    if p_message[0] == '-':
        return "Command not found try '-help'"
    
    return

