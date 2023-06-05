##########################################################
def handle_response(message, username) -> str:
    p_message = message.lower()

    #Display all options
    if p_message == "help" or p_message == '-h' or p_message == 'h' or p_message == '-help':
        return "Default help message"

    return

