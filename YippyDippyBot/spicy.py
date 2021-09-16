def get_nhentai_link(message_components):
    if(len(message_components) == 2):
        message = message_components[1]

        if not(message.isdigit()):
            message = "177013"
    
    return "https://nhentai.net/g/{}".format(message)