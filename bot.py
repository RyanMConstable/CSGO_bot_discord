import discord
import responses
import os
import view

#Creates a discord embed to prettify results and send to user discord
async def send_message(username, message, user_message, usernameID, is_private = False):
    try:
        response = responses.handle_response(user_message, username, usernameID)
        if response == None:
            return
        embed = discord.Embed(title = "", description = F"```\n{response}\n```")
        embed.add_field(name = "", value = "")
        if len(embed) > 4096:
            await message.author.send(F"```\n{response}\n```") if is_private else await message.channel.send(F"```\n{response}\n```")
        else:
            await message.author.send(embed=embed) if is_private else await message.channel.send(embed = embed)
    except Exception as e:
        return

def run_discord_bot():
    TOKEN = os.environ["DISCORD_TOKEN"]
    bot = discord.Bot(intents=discord.Intents.all())
    
    @bot.event
    async def on_message(message):
        if message.author != bot.user or message.content != "-Summary Time":
            return

        usernameID = str(message.author.id)
        username = str(message.author)
        user_message = message.content

        await send_message(username, message, user_message, usernameID, is_private=False)
    
    #Simple notification, notifies that the bot is ready and working
    @bot.event
    async def on_connect():
        print("Connected and ready to go")
    
    #Provides a menu for all of the commands that a user can see
    @bot.slash_command(name = "menu", description="Provides a stat gui")
    async def menu(ctx: discord.ApplicationContext):
        await ctx.respond("", view=view.MyView(ctx))
    
    #Provides a button that links to the signup page
    @bot.slash_command(name = "signup", description="Provides the signup button, links to website")
    async def signup(ctx: discord.ApplicationContext):
        await ctx.respond("", view=view.SignUpView())
    
    bot.run(TOKEN)