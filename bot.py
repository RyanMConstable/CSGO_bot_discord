import discord
import responses
import os
async def send_message(username, message, user_message, usernameID, is_private):
    try:
        response = responses.handle_response(user_message, username, usernameID)
        if response == None:
            return
        #Create an embed for a cleaner feel
        embed = discord.Embed(title = "")
        embed.add_field(name = "", value = "```\n{}\n```".format(response))
        print(len(embed))
        #If the embed is too large then just print normally (although there is a max on that as well)
        if len(embed) > 1024:
            await message.author.send("```\n{}\n```".format(response)) if is_private else await message.channel.send("```\n{}\n```".format(response))
        else:
            await message.author.send(embed=embed) if is_private else await message.channel.send(embed = embed)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.environ["DISCORD_TOKEN"]
    client = discord.Client(intents=discord.Intents.all())
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
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
    client.run(TOKEN)
