from tabulate import tabulate
from table2ascii import table2ascii as t2a, PresetStyle
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
        returnString = "Commands:\n\t  -steamid <id> <steamkey>\n\t  -myavg\n\t  -top <amount> <category>\n\t  -mytop <amount> <category>\n\n    Categories: \n\t[totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown, molly_thrown, incendiary_thrown, decoy_thrown, round_count]" 
        return returnString 
    
    
    
    #This allows a user to add their steamid to the database for future reference
    if command == "-steamid":
        #Here we should attempt an API call to validate the user...
        try:
            CSGOsql.setDiscordUser(usernameID, p_message.split(" ")[1], message.split(" ")[2].upper())
        except:
            return "Incorrect Input try '-steamid <id> <key>'\nSteam key is found here as 'Authentication key': https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=730&issueid=128"
        return "SteamID updated"
    
    
    
    #Returns the top x (between 0 and 100) for all users in database of a given category
    if command == "-top":
        if len(p_message) == 4:
            result = CSGOsql.findtopstat()
            output = t2a(header=result[1], body=result[0], style=PresetStyle.thin_compact)
            return output
        if len(p_message.split(" ")) == 3:
            try:
                num = p_message.split(" ")[1]
                category = p_message.split(" ")[2]
                result = CSGOsql.findTopX(category, num)
                output = t2a(header=result[1], body=result[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + e)
                return "Incorrect format, try '-top <amount> <category>'"
    
    
    
    
    
    #Returns the top x (between 0 and 100) for the user creating the command of a given category
    if command == "-mytop" or command == "-givetop":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        if len(p_message) == 6 or len(p_message) == 8:
            try:
                topuserinfo = CSGOsql.findusertop(id[0])
                output = t2a(header=topuserinfo[1], body=topuserinfo[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Unexpected Error"
        if len(p_message.split(" ")) == 3:
            try:
                num = p_message.split(" ")[1]
                category = p_message.split(" ")[2]
                updateGames = CSGOsql.findTop10user(category, id[0], num)
                output = t2a(header=updateGames[1], body=updateGames[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Incorrect format, try '-mytop <amount> <category> <optional username>'"
        if len(p_message.split(" ")) == 4:
            try:
                num = p_message.split(" ")[1]
                category = p_message.split(" ")[2]
                name = p_message.split(" ")[3]
                foundid = CSGOsql.findSteamID2(name)
                updateGames = CSGOsql.findTop10user(category, foundid, num)
                output = t2a(header=updateGames[1], body=updateGames[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Incorrect format, try '-mytop <amount> <category> <optional username>'"
    
    #Gives the user their average, there should be a simpler command for this in the backend...
    if command == "-myavg":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        if len(p_message.split(" ")) == 1:
            try:
                csgoReturn = CSGOsql.findAvg(id[0])
                head = csgoReturn[0]
                strVal = csgoReturn[1]
                output = t2a(header=head, body=strVal, style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + e)
                return "Error, most likely invalid steamid/steam key"
        if len(p_message.split(" ")) == 2:
            try:
                name = p_message.split(" ")[1]
                foundid = CSGOsql.findSteamID2(name)
                csgoReturn = CSGOsql.findAvg(foundid)
                strVal = csgoReturn[1]
                output = t2a(header=["Category", name], body=strVal, style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + e)
                return "Error, most likely invalid steamid/steam key"
    
    #If user uses a - and it wasn't caught by previous statements, let them know the command was invalid
    if p_message[0] == '-':
        return "Command not found try '-help'"
    
    return

