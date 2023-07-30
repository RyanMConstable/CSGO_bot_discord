import discord, responses

#View for menu buttons
class MyView(discord.ui.View):
    def __init__(self, ctx=None, user=None):
        super().__init__()
        self.ctx = ctx
        if user is None:
            self.user = str(self.ctx.author)
        else:
            self.user = user
        
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
        msg = responses.handle_response("-bottom 50 adr", str(self.ctx.author), self.ctx.author.id)
        await interaction.response.send_message(embed=self.makeEmbed(msg))