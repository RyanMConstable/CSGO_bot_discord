import discord
import responses
import os

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
    
    @client.event
    async def on_message(message):
        #This is used in case the bot should not respond to itself
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
        
        
        
        
    #View for menu buttons
    class MyView(discord.ui.View):
        def __init__(self, ctx=None):
            super().__init__()
            self.ctx = ctx
        
        def makeEmbed(self, msg):
            embed = discord.Embed(title = "", description = F"```\n{msg}\n```")
            embed.add_field(name = "", value = "")
            return embed
        
        @discord.ui.button(label="Top Stats", style=discord.ButtonStyle.primary)
        async def first_button_callback(self, button, interaction):
            msg = responses.handle_response("-top", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Leaderboard", style=discord.ButtonStyle.primary)
        async def second_button_callback(self, button, interaction):
            msg = responses.handle_response("-leaders", self.ctx.author, self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Position", style=discord.ButtonStyle.primary)
        async def third_button_callback(self, button, interaction):
            msg = responses.handle_response("-pos", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Last Game", style=discord.ButtonStyle.primary)
        async def fourth_button_callback(self, button, interaction):
            msg = responses.handle_response("-lastgame", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Best Game", style=discord.ButtonStyle.primary)
        async def fifth_button_callback(self, button, interaction):
            msg = responses.handle_response("-bestgame", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Worst Game", style=discord.ButtonStyle.primary)
        async def sixth_button_callback(self, button, interaction):
            msg = responses.handle_response("-worstgame", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Average Stats", style=discord.ButtonStyle.primary)
        async def seventh_button_callback(self, button, interaction):
            msg = responses.handle_response("-avg", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Totals", style=discord.ButtonStyle.primary)
        async def eighth_button_callback(self, button, interaction):
            msg = responses.handle_response("-sum", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
            
        @discord.ui.button(label="Summary of Last Game", style=discord.ButtonStyle.primary)
        async def ninth_button_callback(self, button, interaction):
            msg = responses.handle_response("-summary", str(self.ctx.author), self.ctx.author.id)
            await interaction.response.send_message(embed=self.makeEmbed(msg))
        
        @discord.ui.button(label="Bottom Stats", style=discord.ButtonStyle.primary)
        async def tenth_button_callback(self, button, interaction):
            await send_message("")
    
    @client.slash_command() # Create a slash command
    async def menu(ctx):
        await ctx.respond("", view=MyView(ctx))
        
    @client.slash_command() # Create a slash command
    async def button(ctx):
        await ctx.respond("", view=MyView(ctx))
    
    client.run(TOKEN)