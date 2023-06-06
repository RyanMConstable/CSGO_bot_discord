import sys
sys.path.append('..')
import CSGO_Project as CSGO

##########################################################
def handle_response(message, username, usernameID) -> str:
    p_message = message.lower()

    #Display all options
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        returnString = "-SteamID <id>" 
        return returnString 
    
    if p_message.split(" ")[0] == "-steamid":
        return "I currently do nothing"

    return

