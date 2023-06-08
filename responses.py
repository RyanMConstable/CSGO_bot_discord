import sys
sys.path.append('..')
import CSGO_Project.CSGOsql
import CSGO_Project.findMatchSteamAPI
import CSGO_Project.getJSONInfo

##########################################################
def handle_response(message, username, usernameID) -> str:
    p_message = message.lower()
    try:
        command = p_message.split(" ")[0].lower()
    except:
        command = None

    #Display help messages
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        returnString = "Commands:\n  -steamid <id>\n  -top10 <category>\n  -topuser10 <category>\n    Categories: [totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown, molly_thrown, incendiary_thrown, decoy_thrown, round_count]" 
        return returnString 
    
    
    
    #This allows a user to add their steamid to the database for future reference
    if command == "-steamid":
        CSGO_Project.CSGOsql.setDiscordUser(usernameID, p_message.split(" ")[1])
        return "SteamID updated"
    
    
    
    #Easy commands to find stats for
    if command == "-top":
        try:
            num = p_message.split(" ")[1]
            category = p_message.split(" ")[2]
            return CSGO_Project.CSGOsql.findTopX(category, num)
        except Exception as e:
            print(e)
            return "Incorrect format, try '-top <amount> <category>'"
    
    
    
    
    
    
    #Specific user commands
    if command == "-topuser10":
        id = CSGO_Project.CSGOsql.findSteamID(usernameID)
        if id is None:
            return "Can't find an id linked with your discord? Use '-steamid <id>'"
        category = p_message.split(" ")[1]
        return CSGO_Project.CSGOsql.findTop10user(category, id)
            
    if command == "-updategames":
        id = CSGO_Project.CSGOsql.findSteamID(usernameID)
        if id is None or id == []:
            return "Can't find an id linked with your discord? Use '-steamid <id>'"
        CSGO_Project.CSGOsql.updateGames(id)
        return "Updating games"
    
    
    return

