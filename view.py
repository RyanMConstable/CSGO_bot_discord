import discord, responses, CSGOsql

#View for menu buttons, the class includes login for the database as well
class MyView(discord.ui.View):
    def __init__(self, ctx=None, enteredUser=None):
        super().__init__(timeout=30)
        self.ctx = ctx
        self.user = str(self.ctx.author)
        self.userid = ctx.author.id
        self.enteredUser = enteredUser
        
        myid = CSGOsql.findSteamID2(self.enteredUser)
        if myid != None and CSGOsql.findDiscordID(myid) != None and self.enteredUser != None:
            self.searchUserID = CSGOsql.findDiscordID(CSGOsql.findSteamID2(self.enteredUser))
            self.searchUserName = self.enteredUser
        else:
            self.searchUserID = self.userid
            self.searchUserName = self.user
        
        button = discord.ui.Button(label ="Steam Login", style=discord.ButtonStyle.url, url = "http://localhost:5000")
        self.add_item(button)
        
    def makeEmbed(self, msg):
        embed = discord.Embed(title = "", description = F"```\n{msg}\n```")
        embed.add_field(name = "", value = "")
        return embed
    
    @discord.ui.button(label="Top Stats", style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        msg = responses.handle_response("-top", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Leaderboard", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        msg = responses.handle_response("-leaders", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Position", style=discord.ButtonStyle.primary)
    async def third_button_callback(self, button, interaction):
        msg = responses.handle_response("-pos", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Last Game", style=discord.ButtonStyle.primary)
    async def fourth_button_callback(self, button, interaction):
        msg = responses.handle_response("-lastgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Best Game", style=discord.ButtonStyle.primary)
    async def fifth_button_callback(self, button, interaction):
        msg = responses.handle_response("-bestgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Worst Game", style=discord.ButtonStyle.primary)
    async def sixth_button_callback(self, button, interaction):
        msg = responses.handle_response("-worstgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Average Stats", style=discord.ButtonStyle.primary)
    async def seventh_button_callback(self, button, interaction):
        msg = responses.handle_response("-avg", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Totals", style=discord.ButtonStyle.primary)
    async def eighth_button_callback(self, button, interaction):
        msg = responses.handle_response("-sum", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Summary of Last Game", style=discord.ButtonStyle.primary)
    async def ninth_button_callback(self, button, interaction):
        msg = responses.handle_response("-summary", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
    
    @discord.ui.button(label="Bottom Stats", style=discord.ButtonStyle.primary)
    async def tenth_button_callback(self, button, interaction):
        msg = responses.handle_response("-bottom 50 adr", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))