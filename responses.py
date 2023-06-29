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
        returnString = "Commands:\n\t  -steamid <id> <steamkey>\n\t  -avg <optional Steam User>\n\t  -top <optional Steam User> <optional amount> <optional category> <optional Steam User>\n\t  -leaders <optional amount> <optional category>\n\n    Categories: \n\t[totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown, molly_thrown, incendiary_thrown, decoy_thrown, round_count, adr, clutches, clutch_won_count, clutch_loss_count, entry_kill_won_count, entry_kill_loss_count, entry_hold_kill_won_count, entry_hold_kill_loss_count, rank_old, rank_new, total_health_damage, total_armor_damage, total_health_damage_taken, total_armor_damage_taken, kill_per_round, assist_per_round, death_per_round, total_time_death, avg_time_death, 1v1_won_count, 1v2_won_count, 1v3_won_count, 1v4_won_count, 1v5_won_count, 1v1_loss_count, 1v2_loss_count, 1v3_loss_count, 1v4_loss_count, 1v5_loss_count, 1v1_count, 1v2_count, 1v3_count, 1v4_count, 1v4_count]" 
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
    if command == "-leaders":
        if len(p_message) == 8:
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
                return "Incorrect format, try '-leaders <amount> <category>'"
    
    
    
    
    
    #Returns the top x (between 0 and 100) for the user creating the command of a given category
    if command == "-top" or command == "-givetop":
        id = CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid' first"
        if len(p_message) == 4 or len(p_message) == 8:
            try:
                topuserinfo = CSGOsql.findusertop(id[0])
                output = t2a(header=topuserinfo[1], body=topuserinfo[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Unexpected Error"
        if len(p_message.split(" ")) == 2:
            try:
                name = p_message.split(" ")[1]
                foundid = CSGOsql.findSteamID2(name)
                topuserinfo = CSGOsql.findusertop(foundid)
                output = t2a(header=topuserinfo[1], body=topuserinfo[0], style=PresetStyle.thin_compact)
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Incorrect format, try '-top <amount> <category> <optional username>'"
        if len(p_message.split(" ")) == 3:
            try:
                num = p_message.split(" ")[1]
                category = p_message.split(" ")[2]
                updateGames = CSGOsql.findTopUser(category, id[0], num)
                output = t2a(header=["Highest {}".format(category)], body=updateGames[0], style=PresetStyle.thin_compact, footer=[username.split("#")[0] + "'s games"])
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Incorrect format, try '-top <amount> <category> <optional username>'"
        if len(p_message.split(" ")) == 4:
            try:
                num = p_message.split(" ")[1]
                category = p_message.split(" ")[2]
                name = p_message.split(" ")[3]
                foundid = CSGOsql.findSteamID2(name)
                updateGames = CSGOsql.findTopUser(category, foundid, num)
                output = t2a(header=["Highest {}".format(category)], body=updateGames[0], style=PresetStyle.thin_compact, footer=[name + "'s games"])
                return output
            except Exception as e:
                print("ERROR IN responses.py: " + str(e))
                return "Incorrect format, try '-top <amount> <category> <optional username>'"
    
    #Gives the user their average, there should be a simpler command for this in the backend...
    if command == "-avg":
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
        return "Command not found try '-help' or '-h'"
    
    return

