#@bot.command(name="gif")
#async def on_gif(ctx):
    #"""
    #Runs when the !gif command was issued in a Discord text channel and posts a 
    #random GIF from the JSON file
    #"""
    #guild = ctx.guild
    #channel = ctx.channel
    #author = ctx.author
    #command = ctx.message.content
    #command_test = ctx.message
    #test = ctx

    ## log event on command line
    #print(f'* "{author.name}" issued "{command}" in "{channel}" of "{guild}"')
    #print("  ctx.message  {}    ".format(command_test))
    #print("  ctx  {}    ".format(command_test))

    ## post random GIF from the JSON file
    #await channel.send(get_random_gif_link())


#def get_random_gif_link():
    #""" Returns a random gif link from the JSON file """
    #with open(JSON_FILE) as json_file:
        ## open JSON file
        #data = json.load(json_file)
        ## get all gifs
        #gifs = data['gifs']
        ## randomly select a gif
        #gif = random.choice(gifs)

        ## return the link of the gif to the caller
        #return gif['link']