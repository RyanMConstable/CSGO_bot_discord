from table2ascii import table2ascii as t2a, PresetStyle
from CSGO_Project import CSGOsql

#This file contains functions that get executed for the responses.py file

#Dictionary: keys = the pretty command the user types in 
#            items are the column names in the db
commandsToCol = {}
commandsToCol["kills"] = "totalkills"
commandsToCol["totalkills"] = "totalkills"
commandsToCol["kill"] = "totalkills"
commandsToCol["score"] = "score"
commandsToCol["teamkills"] = "tk_count"
commandsToCol["tk"] = "tk_count"
commandsToCol["assists"] = "assist"
commandsToCol["deaths"] = "deaths"
commandsToCol["5k"] = "5k"
commandsToCol["4k"] = "4k"
commandsToCol["3k"] = "3k"
commandsToCol["2k"] = "2k"
commandsToCol["1k"] = "1k"
commandsToCol["headshots"] = "headshot"
commandsToCol["head"] = "headshot"
commandsToCol["hd"] = "headshot"
commandsToCol["kd"] = "kd"
commandsToCol["rws"] = "rws"
commandsToCol["shotsfired"] = "shot_count"
commandsToCol["shots"] = "shot_count"
commandsToCol["shotslanded"] = "hit_count"
commandsToCol["flashes"] = "flashbang_thrown"
commandsToCol["smokes"] = "smoke_thrown"
commandsToCol["he"] = "he_thrown"
commandsToCol["mollys"] = "molly_trown"
commandsToCol["incens"] = "incendiary_thrown"
commandsToCol["decoys"] = "decoy_thrown"
commandsToCol["rounds"] = "round_count"
commandsToCol["adr"] = "adr"
commandsToCol["clutches"] = "clutches"
commandsToCol["clutcheswon"] = "clutch_won_count"
commandsToCol["clutcheslost"] = "clutch_loss_count"
commandsToCol["entrykills"] = "entry_kill_won_count"
commandsToCol["entrydeaths"] = "entry_kill_loss_count"
commandsToCol["entriesdenied"] = "entry_hold_kill_won_count"
commandsToCol["entriesgiven"] = "entry_hold_kill_loss_count"
commandsToCol["oldrank"] = "rank_old"
commandsToCol["newrank"] = "rank_new"
commandsToCol["totaldamage"] = "total_health_damage"
commandsToCol["damage"] = "total_health_damage"
commandsToCol["totalarmordamage"] = "total_armor_damage"
commandsToCol["tad"] = "total_armor_damage"
commandsToCol["totaldamagetaken"] = "total_health_damage_taken"
commandsToCol["tdt"] = "total_health_damage_taken"
commandsToCol["totalarmordamagetaken"] = "total_armor_damage_taken"
commandsToCol["tadt"] = "total_armor_damage_taken"
commandsToCol["killperround"] = "kill_per_round"
commandsToCol["kpr"] = "kill_per_round"
commandsToCol["assistperround"] = "assist_per_round"
commandsToCol["apr"] = "assist_per_round"
commandsToCol["deathperround"] = "death_per_round"
commandsToCol["dpr"] = "death_per_round"
commandsToCol["totaldeathtime"] = "total_time_death"
commandsToCol["deathtime"] = "total_time_death"
commandsToCol["avgdeathtime"] = "avg_time_death"
commandsToCol["1v1won"] = "1v1_won_count"
commandsToCol["1v2won"] = "1v2_won_count"
commandsToCol["1v3won"] = "1v3_won_count"
commandsToCol["1v4won"] = "1v4_won_count"
commandsToCol["1v5won"] = "1v5_won_count"
commandsToCol["1v1loss"] = "1v1_loss_count"
commandsToCol["1v2loss"] = "1v2_loss_count"
commandsToCol["1v3loss"] = "1v3_loss_count"
commandsToCol["1v4loss"] = "1v4_loss_count"
commandsToCol["1v5loss"] = "1v5_loss_count"
commandsToCol["1v1total"] = "1v1_count"
commandsToCol["1v2total"] = "1v2_count"
commandsToCol["1v3total"] = "1v3_count"
commandsToCol["1v4total"] = "1v4_count"
commandsToCol["1v5total"] = "1v5_count"

#Display help message tp the user
def help():
    commands = "Commands:\n\t"
    commands += "-steamid <id> <steamkey>\n\t"
    commands += "avg <optional steam user>\n\t"
    commands += "top <optional amount> <optional category> <optional steam user>\n\t"
    commands += "-leaders <optional amount> <optional category>\n\n"
    commands += "Categories:\n\t"
      

    dictionaryKeys = []
    for key in commandsToCol:
        dictionaryKeys.append(key)
    
    return commands + str(dictionaryKeys)


#Add your steamid to the database so it tracks your games
def steamid(discordID, message):
    try:
        steamID = message.split(" ")[1]
        steamKEY = message.split(" ")[2]
        CSGOsql.setDiscordUser(discordID, steamID, steamKEY)
    except:
        errorMSG = "Incorrect Input try '-steamid <id> <key>'\n"
        errorMSG += "Steam key is found here as 'Authentication key': "
        errorMSG += "https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=730&issueid=128"
        return errorMSG
    return "SteamID updated"


#For the top all time leaders of categories
def leaders(fullCommand):
    if fullCommand == "-leaders":
        result = CSGOsql.findtopstat()
    elif len(fullCommand.split(" ")) == 3:
        try:
            num = fullCommand.split(" ")[1]
            category = commandsToCol[fullCommand.split(" ")[2]]
            result = CSGOsql.findTopX(category, num)
        except Exception as e:
            #os.system("echo [ERROR] in leaders function: {} >> responsesLOG.txt".format(e))
            return "Incorrect format, try '-leaders <amount> <category>'"
    else:
        return "Invalid command use '-h' for help"
    return t2a(header=result[1], body=result[0], style=PresetStyle.thin_compact)


#For the average of the given users
def avg(userID, fullCommand, discordName):
    commandLength = len(fullCommand.split(" "))
    
    if fullCommand == '-avg':
        name = discordName.split("#")[0]
        steamid = CSGOsql.findSteamID(userID)[0]
    elif commandLength == 2:
        name = fullCommand.split(" ")[1]
        steamid = CSGOsql.findSteamID2(name)
    else:
        return "Invalid Command try '-h' for help"
    
    try:
        tableValues = CSGOsql.findAvg(steamid)
        head = ["Category", name]
        body = tableValues[1]
        return t2a(header=head, body=body, style=PresetStyle.thin_compact)
    except:
        return "Error..."
    
    
#For the top games of the given users
def top(userID, message, discordName):
    name = discordName.split("#")[0]
    commandList = ["-top", "-givetop"]
    commandLen = len(message.split(" "))
    
    steamid = CSGOsql.findSteamID(userID)[0]
    if steamid is None:
        return "Can't find an id linked with your discord? Use '-steamid' first"
    
    if message in commandList or commandLen == 2:
        if commandLen == 2:
            name = message.split(" ")[1]
            steamid = CSGOsql.findSteamID2(name)
        
        topuserinfo = CSGOsql.findusertop(steamid)
        head = topuserinfo[1]
        body = topuserinfo[0]

    elif commandLen == 3 or commandLen == 4:
        if commandLen == 4:
            name = message.split(" ")[3]
            steamid = CSGOsql.findSteamID2(name)
        
        limit = message.split(" ")[1]
        category = commandsToCol[message.split(" ")[2]]
        topGames = CSGOsql.findTopUser(category, steamid, limit)
    
        head = ["Highest {}".format(category)]
        body = topGames[0]        
    return t2a(header=head, body=body, style=PresetStyle.thin_compact)

#This function finds the bottom x users of a given category
def bottom(message):
    try:
        limit = message.split(" ")[1]
        category = commandsToCol[message.split(" ")[2]]
        bottomResults = CSGOsql.findBottom(category, limit)
    except:
        return "Invalid Command"
    
    return t2a(header=[category, "This is bad"], body = bottomResults, style=PresetStyle.thin_compact)