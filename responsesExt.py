from table2ascii import table2ascii as t2a, PresetStyle
import CSGOsql
import formatData, dictCommands

#This file contains functions that get executed for the responses.py file

commandsToCol = dictCommands.commandsToCol



#Display help message tp the user
def help():
    commands = "Commands:\n\t"
    commands += "-steamid <id> <steamkey>\n\t"
    commands += "avg <optional steam user>\n\t"
    commands += "top <optional amount> <optional category> <optional steam user>\n\t"
    commands += "-leaders <optional amount> <optional category>\n\t"
    commands += "-bestgame\n\t"
    commands += "-worstgame\n\t"
    commands += "-pos\n\n"
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
        result = formatData.findtopstat()
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
        print("Steamid: {} Name: {} Limiter: {}".format(steamid, name, limiter))
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


#This function finds the bestgame of a user
def bestgame(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-bestgame":
        tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, "score", "DESC"))
        returnString = "{}'s Best Score Game\n".format(name)
        returnString += "Date: {}\n".format(tableInfo[1])
        returnString += str(t2a(header=["Stats", "Best"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2]
        return returnString
    category = commandsToCol[message.split(" ")[1]]
    tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, category, "DESC"))
    returnString = "{}'s Best Score Game\n".format(name)
    returnString += "Date: {}\n".format(tableInfo[1])
    returnString += str(t2a(header=["Stats", "Best"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
    returnString += tableInfo[2]
    return returnString


#This function finds the worstgame of a user
def worstgame(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-worstgame":
        tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, "score", "ASC"))
        returnString = "{}'s Worst Score Game\n".format(name)
        returnString += "Date: {}\n".format(tableInfo[1])
        returnString += str(t2a(header=["Stats", "Worst"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2]
        return returnString
    category = commandsToCol[message.split(" ")[1]]
    tableInfo = formatData.sortGame(CSGOsql.findGameStats(steamid, category, "ASC"))
    returnString = "{}'s Worst Score Game\n".format(name)
    returnString += "Date: {}\n".format(tableInfo[1])
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
        returnString = "{}'s Last Game\n".format(name)
        returnString += "Date: {}\n".format(tableInfo[1])
        returnString += str(t2a(header=["Stats", "Last"], body = tableInfo[0], style=PresetStyle.thin_compact)) + "\n"
        returnString += tableInfo[2]
        return returnString
    return

#This function finds the position of a user
def pos(username, message, userID):
    name = username.split("#")[0]
    steamid = CSGOsql.findSteamID(userID)[0]
    if message == "-pos":
        tableInfo = formatData.posGame(steamid)
        return str(t2a(header = ["Stat", "Pos"], body = tableInfo, style=PresetStyle.thin_compact))
    else:
        category = commandsToCol[message.split(" ")[1]]
        returnString = "You are {} place for the {} category".format(CSGOsql.findPos(steamid, category), category)
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
        print("Steamid: {} Name: {} Limiter: {}".format(steamid, name, limiter))
        tableValues = formatData.findSum(steamid, limiter)
        head = ["Category", name]
        body = tableValues[1]
        return t2a(header=head, body=body, style=PresetStyle.thin_compact)
    except:
        return "Error..."