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
            return tabulate(result[0], result[1], tablefmt="grid")
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGOsql.findTopX(category, num)
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Incorrect format, try '-top <amount> <category>'"
    
    
    
    
    
    #Returns the top x (between 0 and 100) for the user creating the command of a given category
    if command == "-mytop":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        if len(p_message) == 6:
            try:
                topuserinfo = CSGOsql.findusertop(id[0])
                return tabulate(topuserinfo[0], headers=topuserinfo[1], tablefmt="grid")
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Unexpected Error"
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGOsql.findTop10user(category, id[0], num)
        except Exception as e:
            print("ERROR IN responses.py: " + str(e))
            return "Incorrect format, try '-mytop <amount> <category>'"
    
    #Gives the user their average, there should be a simpler command for this in the backend...
    if command == "-myavg":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        try:
            strVal = []
            strVal.append(["Total Games", str(CSGOsql.findNumberOfGames(id[0]))])
            strVal.append(["Kills", str(CSGOsql.selectAvgUserStat("totalkills", id[0]))])
            strVal.append(["Score", str(CSGOsql.selectAvgUserStat("score", id[0]))])
            strVal.append(["Team Kills", str(CSGOsql.selectAvgUserStat("tk_count", id[0]))])
            strVal.append(["Assists", str(CSGOsql.selectAvgUserStat("assist", id[0]))])
            strVal.append(["Deaths", str(CSGOsql.selectAvgUserStat("deaths", id[0]))])
            strVal.append(["Headshots", str(CSGOsql.selectAvgUserStat("headshot", id[0]))])
            strVal.append(["KD", str(CSGOsql.selectAvgUserStat("kd", id[0]))])
            strVal.append(["RWS", str(CSGOsql.selectAvgUserStat("rws", id[0]))])
            strVal.append(["Shot Count", str(CSGOsql.selectAvgUserStat("shot_count", id[0]))])
            strVal.append(["Hit Count", str(CSGOsql.selectAvgUserStat("hit_count", id[0]))])
            
            head = ["Category", "Average"]
            return tabulate(strVal, head, tablefmt="grid")
        except Exception as e:
            print("ERROR IN responses.py: " + e)
            return "Error, most likely invalid steamid/steam key"
    
    #If user uses a - and it wasn't caught by previous statements, let them know the command was invalid
    if p_message[0] == '-':
        return "Command not found try '-help'"
    
    return

