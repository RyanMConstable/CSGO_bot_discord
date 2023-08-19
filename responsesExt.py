from table2ascii import table2ascii as t2a, PresetStyle
import CSGOsql
import formatData, dictCommands

#This file contains functions that get executed for the responses.py file

commandsToCol = dictCommands.commandsToCol



#Display help message tp the user
def help():
    commands = "Commands:\n\t"
    commands += "avg <optional steam user>\n\t"
    commands += "top <optional amount> <optional category> <optional steam user>\n\t"
    commands += "-leaders <optional amount> <optional category>\n\t"
    commands += "-bestgame\n\t"
    commands += "-worstgame\n\t"
    commands += "-pos\n\t"
    commands += "-sum\n\t"
    commands += "-summary\n\t"
    commands += "-lastgame\n\t"
    commands += "-bestgame\n\t"
    commands += "-worstgame\n\t"
    commands += "/menu <name>\n\n"
    
    commands += "Categories:\n\t"
      

    dictionaryKeys = []
    for key in commandsToCol:
        dictionaryKeys.append(key)
    
    return commands + str(dictionaryKeys)



#For the top all time leaders of categories
#The best of the best
def leaders(fullCommand):
    if fullCommand == "-leaders":
        result = formatData.findtopstat()
    elif len(fullCommand.split(" ")) == 3:
        try:
            num = fullCommand.split(" ")[1]
            category = commandsToCol[fullCommand.split(" ")[2]]
            result = [CSGOsql.findTopX(category, num), ["Name", category]]
        except Exception as e:
            #os.system(F"echo [ERROR] in leaders function: {e} >> responsesLOG.txt")
            return "Incorrect format, try '-leaders <amount> <category>'"
    else:
        return "Invalid command use '-h' for help"
    return t2a(header=result[1], body=result[0], style=PresetStyle.thin_compact)



#For the average of the given users
#Updated the users avg games
def avg(userID, fullCommand, discordName):
    commandLength = len(fullCommand.split(" "))
    
    limiter = '50000'
    name = discordName.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
                
    if commandLength >= 2:
        if fullCommand.split(" ")[-1].isdigit() == False:
            name = ' '.join(fullCommand.split(" ")[1:])
            steamid = CSGOsql.findSteamID2(name)
        else:
            limiter = fullCommand.split(" ")[commandLength-1]
            if commandLength != 2:
                name = ' '.join(fullCommand.split(" ")[1:commandLength-1])
                steamid = CSGOsql.findSteamID2(name)   
    
    try:
        tableValues = formatData.findAvg(steamid, limiter)
        head = ["Category", name]
        body = tableValues[1]
        return t2a(header=head, body=body, style=PresetStyle.thin_compact)
    except:
        return "Error..."
    
    
    
#For the top games of the given users
#Returns the users best games!
def top(userID, message, discordName):
    name = discordName.split("#")[0]
    commandList = ["-top", "-givetop"]
    commandLen = len(message.split(" "))
    
    steamid = CSGOsql.findSteamID(userID)[0]
    if steamid is None:
        return "Can't find an id linked with your discord? Use '-steamid' first"
    
    if commandLen > 1:
        name = ' '.join(message.split(" ")[1:])
        testid = CSGOsql.findSteamID2(name)
    
    if message in commandList or testid is not None:
        if commandLen == 2:
            steamid = testid
        
        topuserinfo = formatData.findusertop(steamid)
        head = topuserinfo[1]
        body = topuserinfo[0]

    elif commandLen >= 3:
        if commandLen >= 4:
            name = ' '.join(message.split(" ")[3:])
            steamid = CSGOsql.findSteamID2(name)
        
        limit = message.split(" ")[1]
        category = commandsToCol[message.split(" ")[2]]
        topGames = CSGOsql.findTopUser(category, steamid, limit)
    
        head = [F"Highest {category}"]
        body = topGames        
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


#This function finds the bestgame of a user
def bestgame(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-bestgame":
        tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, "score", "DESC"))
        returnString = F"{name}'s Best Score Game\n"
        returnString += F"Date: {tableInfo[1]}\n"
        returnString += str(t2a(header=["Stats", "Best"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2]
        return returnString
    category = commandsToCol[message.split(" ")[1]]
    tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, category, "DESC"))
    returnString = F"{name}'s Best Score Game\n"
    returnString += F"Date: {tableInfo[1]}\n"
    returnString += str(t2a(header=["Stats", "Best"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
    returnString += tableInfo[2]
    return returnString


#This function finds the worstgame of a user
def worstgame(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-worstgame":
        tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, "score", "ASC"))
        returnString = F"{name}'s Worst Score Game\n"
        returnString += F"Date: {tableInfo[1]}\n"
        returnString += str(t2a(header=["Stats", "Worst"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2]
        return returnString
    category = commandsToCol[message.split(" ")[1]]
    tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, category, "ASC"))
    returnString = F"{name}'s Worst Score Game\n"
    returnString += F"Date: {tableInfo[1]}\n"
    returnString += str(t2a(header=["Stats", "Worst"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
    returnString += tableInfo[2]
    return returnString


#This function finds the lastgame of a user
#It then returns the table of data
def lastgame(username, message, userID):
    name = username.split("#")[0]
    if message == "-lastgame":
        steamid = CSGOsql.findSteamID(userID)[0]
        tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, "date", "DESC"))
        returnString = F"{name}'s Last Game\n"
        returnString += F"Date: {tableInfo[1]}\n"
        returnString += str(t2a(header=["Stats", "Last"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2] + "\n"
        
        gameinfo = CSGOsql.findGameInfoLastGame()
        importantGameInfo = [["Game Length", str(float(gameinfo[1])/60)], ["Map", gameinfo[2].split("_")[1]], ["Score", str(gameinfo[3]) + ":" + str(gameinfo[4])]]
        returnString += str(t2a(body = importantGameInfo, style=PresetStyle.thin_compact))
        return returnString
    return

#This function finds the position of a user
def pos(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-pos":
        tableInfo = formatData.posGame(steamid)
        return str(t2a(header = ["Stat", "Pos", "%"], body = tableInfo, style=PresetStyle.thin_compact))
    else:
        category = commandsToCol[message.split(" ")[1]]
        returnString = F"You are {CSGOsql.findPos(steamid, category)} place for the {category} category"
    return returnString

#This function finds finds the sum
#This is current a copy of avg, need to refactor
def sum(userID, fullCommand, discordName):
    commandLength = len(fullCommand.split(" "))
    
    limiter = '50000'
    name = discordName.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
                
    if commandLength >= 2:
        if fullCommand.split(" ")[-1].isdigit() == False:
            name = ' '.join(fullCommand.split(" ")[1:])
            steamid = CSGOsql.findSteamID2(name)
        else:
            limiter = fullCommand.split(" ")[commandLength-1]
            if commandLength != 2:
                name = ' '.join(fullCommand.split(" ")[1:commandLength-1])
                steamid = CSGOsql.findSteamID2(name)   
    
    try:
        tableValues = formatData.findSum(steamid, limiter)
        head = ["Category", name]
        body = tableValues[1]
        return t2a(header=head, body=body, style=PresetStyle.thin_compact)
    except:
        return "Error..."
    
#This function will print a summary to the user
def summary():
    #If a user is below 50 adr, bozo alert is handed out
    #Return top adr, bottom adr
    recentGameInfo = CSGOsql.findGameInfo()
    lowlowADRList = []
    lowADRList = []
    highADRList = []
    highest_team_damage = [None, 0]
    highest_team_kills = []
    flashes = []
    uniquemsgs = []

    for gamer in recentGameInfo:
        
        #ADR
        if float(gamer[1]) <= 35:
            lowlowADRList.append([gamer[0]])
        elif float(gamer[1]) <= 50:
            lowADRList.append([gamer[0]])
        elif float(gamer[1]) >= 115:
            highADRList.append([gamer[0]])
            
        #Team damage
        if int(gamer[2]) > highest_team_damage[1]:
            highest_team_damage = [gamer[0], int(gamer[2])]
            
        #Team kills
        if int(gamer[3]) >= 2:
            highest_team_kills.append([gamer[0]])
            
        #Flashes
        if int(gamer[4]) >= int(gamer[5]) or float(gamer[6]) >= float(gamer[7]):
            flashes.append([gamer[0], gamer[4], gamer[5], gamer[6], gamer[7]])
        
        #Messages
        if int(gamer[8]) >= 30:
            uniquemsgs.append([gamer[0], gamer[8]])
            
    head = ["The Bozos"]
    body = lowADRList
    lowadrtable = ""
    if any(body):
        lowadrtable = t2a(header=head, body=body, style=PresetStyle.thin_compact)
        
    head = ["The Super Bozos"]
    body = lowlowADRList
    lowlowadrtable = ""
    if any(body):
        lowlowadrtable = t2a(header=head, body=body, style=PresetStyle.thin_compact)
    
    head = ["Super Gamers"]
    body = highADRList
    highadrtable = ""
    if any(body):
        highadrtable = t2a(header=head, body=body, style=PresetStyle.thin_compact)
    
    teamdamagetable = ''
    if highest_team_damage[0] != None:
        head = ["The Real Enemy"]
        body = [[str(highest_team_damage[0]) + ": " + str(highest_team_damage[1]) + " dmg"]]
        teamdamagetable = t2a(header=head, body=body, style=PresetStyle.thin_compact)
        
    head = ["Teammate Terminators"]
    body = highest_team_kills
    highteamkillstable = ""
    if any(body):
        highteamkillstable = t2a(header=head, body=body, style=PresetStyle.thin_compact)
    
    
    flashtable = ''
    if highest_team_damage[0] != None:
        head = ["Feebleminded Flashbangers", "Team", "Enemy", "Team", "Enemy"]
        body = flashes
        footer = ["Feebleminded Flashbangers", "Count", "Count", "Dur", "Dur"]
        flashtable = t2a(header=head, body=body, footer=footer, style=PresetStyle.thin_compact)

    #First find the game id for 
    return lowlowadrtable + "\n" + lowadrtable + "\n" + highadrtable + "\n" + teamdamagetable + "\n" + highteamkillstable + "\n" + flashtable