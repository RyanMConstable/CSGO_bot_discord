import discord
import responses
import os
import view

async def send_message(username, message, user_message, usernameID, is_private = False):
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
    
    #viewcommands = client.create_group("viewcommands", "Button views")
    
    @client.event
    async def on_message(message):
        #This is used in case the bot should not respond to itself
        if message.author == client.user and message.content != "-Summary Time":
            return

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
    
    @client.command(name = "sync")
    async def sync(ctx):
        await client.sync_commands()
        await ctx.respond("Synced commands")
    
    @client.command(name = "menu", description="Provides a stat gui") # Create a menu command
    async def menu(ctx: discord.ApplicationContext):
        await ctx.respond("", view=view.MyView(ctx))
        
    @client.command(name = "signup", description="Provides the signup menu") #Sign up view
    async def signup(ctx):
        await ctx.respond("", view=view.SignUpView())
    
    client.run(TOKEN)