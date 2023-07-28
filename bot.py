import discord
import responses
import os

async def send_message(username, message, user_message, usernameID, is_private):
    try:
        response = responses.handle_response(user_message, username, usernameID)
        if response == None:
            return
        #Create an embed for a cleaner feel
        embed = discord.Embed(title = "", description = F"```\n{response}\n```")
        embed.add_field(name = "", value = "")
        print(len(embed))
        #If the embed is too large then just print normally (although there is a max on that as well)
        if len(embed) > 4096:
            await message.author.send(F"```\n{response}\n```") if is_private else await message.channel.send(F"```\n{response}\n```")
        else:
            await message.author.send(embed=embed) if is_private else await message.channel.send(embed = embed)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.environ["DISCORD_TOKEN"]
    client = discord.Bot(intents=discord.Intents.all())
    
    @client.event
    async def on_message(message):
        #This is used in case the bot should not respond to itself
        #if message.author == client.user:
            #return

        usernameID = str(message.author.id)
        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        #this sends the user a dm
        #await send_message(username, message, user_message, is_private=True)

        #this sends in the discord
        await send_message(username, message, user_message, usernameID, is_private=False)
    
    #Testing on_typing event   
    #@client.event
    #async def on_typing(channel, user, when):
    #    print(F"User: {user} is typing in channel: {channel} at: {when}"
        
    #Testing on_raw_typing event   
    #@client.event
    #async def on_raw_typing(payload):
    #    print(payload)
        
    @client.event
    async def on_connect():
        print("Connected and ready to go")
        
    @client.event
    async def on_disconnect():
        print("Going dark")
        
    class MyView(discord.ui.View):
        def __init__(self, userid=None):
            super().__init__()
            self.userid = userid
            
        @discord.ui.button(label="Your Best Stats", style=discord.ButtonStyle.primary)
        async def first_button_callback(self, button, interaction):
            await interaction.response.send_message("ewewfawefawef") 
            
        @discord.ui.button(label="Leaders", style=discord.ButtonStyle.primary)
        async def second_button_callback(self, button, interaction):
            await interaction.response.send_message("Leader") 
    
    @client.slash_command() # Create a slash command
    async def button(ctx, message):
        await ctx.respond("", view=MyView(ctx.author.id))
        
    @client.command() # Create a slash command
    async def menu(ctx, message):
        await ctx.respond("", view=MyView(ctx.author.id))
    
    client.run(TOKEN)