import discord, responses, CSGOsql

#GUI for the statistic commands, TODO Look at more pretty ways of doing this
class MyMenu(discord.ui.View):
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
        
    @discord.ui.button(label="Position", row = 1, style=discord.ButtonStyle.primary)
    async def third_button_callback(self, button, interaction):
        msg = responses.handle_response("-pos", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Last Game", row = 1, style=discord.ButtonStyle.primary)
    async def fourth_button_callback(self, button, interaction):
        msg = responses.handle_response("-lastgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Best Game", row = 2, style=discord.ButtonStyle.primary)
    async def fifth_button_callback(self, button, interaction):
        msg = responses.handle_response("-bestgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Worst Game", row = 2, style=discord.ButtonStyle.primary)
    async def sixth_button_callback(self, button, interaction):
        msg = responses.handle_response("-worstgame", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Average Stats", row = 3, style=discord.ButtonStyle.primary)
    async def seventh_button_callback(self, button, interaction):
        msg = responses.handle_response("-avg", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Totals", row = 4, style=discord.ButtonStyle.primary)
    async def eighth_button_callback(self, button, interaction):
        msg = responses.handle_response("-sum", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
    @discord.ui.button(label="Summary of Last Game", row = 4, style=discord.ButtonStyle.primary)
    async def ninth_button_callback(self, button, interaction):
        msg = responses.handle_response("-summary", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
    
    @discord.ui.button(label="Bottom Stats", row=3, style=discord.ButtonStyle.primary)
    async def tenth_button_callback(self, button, interaction):
        msg = responses.handle_response("-bottom 50 adr", self.searchUserName, self.searchUserID)
        await interaction.response.send_message(embed=self.makeEmbed(msg))
        
        
#This view is just a link to the login website, need a domain eventually instead of the raw ip TODO    
class SignUpView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
        button = discord.ui.Button(label="Create Account", style=discord.ButtonStyle.url, url = "http://10.0.0.130")
        self.add_item(button)

#This is the user feedback modal
#Take in suggestions and feedback from the user to mongodb
class userFeedback(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short Input"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        print(self.children[0].value, self.children[1].value)
        await interaction.response.send_message("Thank you for your feedback!")

#This is the modal to return a menu for the user given
#Enter a username into the modal and it returns the menu for stats of that user
class oUserModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Username"))

    async def callback(self, interaction: discord.Interaction):
        print(self.children[0].value)
        await interaction.response.send_message("Return the menu here?")