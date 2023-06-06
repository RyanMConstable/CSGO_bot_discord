import sys
sys.path.append('..')
import CSGO_Project.CSGOsql

##########################################################
def handle_response(message, username, usernameID) -> str:
    p_message = message.lower()
    try:
        command = p_message.split(" ").lower()
    except:
        command = None

    #Display all options
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        returnString = "-SteamID <id>" 
        return returnString 
    
    if command == "-steamid":
        CSGO_Project.CSGOsql.setDiscordUser(usernameID, p_message.split(" ")[1])
        return "SteamID updated"

    return

