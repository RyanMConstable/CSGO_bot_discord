from table2ascii import table2ascii as t2a, PresetStyle
from CSGO_Project import CSGOsql
import responsesExt

##########################################################
def handle_response(message, username, usernameID) -> str:
    #This makes sure that any command in any form of caps is met
    p_message = message.lower()
    try:
        command = p_message.split(" ")[0].lower()
    except:
        command = None
    
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
        return responsesExt.avg(usernameID, p_message, username)
    
    #If user uses a - and it wasn't caught by previous statements, let them know the command was invalid
    if p_message[0] == '-':
        return "Command not found try '-help' or '-h'"
    
    return

