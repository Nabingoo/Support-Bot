import discord
from discord.ext import commands
from discord import Embed
import time
intents = discord.Intents.default()

intents.guilds = True

bot = commands.Bot(command_prefix = ";", intents = intents,change_discord_methods=True)

class WhitelistFunc(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Staking Whitelist', style=discord.ButtonStyle.green)
    async def stakewhite(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "Staking Whitelist"
        self.stop()
    @discord.ui.button(label='Invite Whitelist', style=discord.ButtonStyle.green)
    async def invitewhite(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "Invite Whitelist"
        self.stop()
    @discord.ui.button(label='Other Whitelist', style=discord.ButtonStyle.green)
    async def Whitelist(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "Other Whitelist"
        self.stop()

class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Whitelist', style=discord.ButtonStyle.green)
    async def Whitelist(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "Whitelist"
        self.stop()
    @discord.ui.button(label='Staking', style=discord.ButtonStyle.green)
    async def Staking(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "Staking"
        self.stop()
    @discord.ui.button(label='Get a Mod!', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        
        self.value = "Mod"
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Cancelling', ephemeral=True)
    
        self.value = "Cancel"
        self.stop()

@bot.event
async def on_guild_channel_create(channel):
    time.sleep(1)
    if "ticket" in channel.name:
        view = Buttons()
        await channel.send('What can we help you with today?', view=view)
    # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
            await channel.send('Time Out...')
        elif view.value == "Whitelist":
            
            view = WhitelistFunc()
            await channel.send('What can we help you with today?', view=view)
            await view.wait()
            if view.value == "Staking Whitelist":
                embed = discord.Embed(title="In order to verify please go to this website ", description="Top 10", color=0x00ff00)
                embed=discord.Embed(description= "In order to verify please go to this website https://app.mycrypto.com/sign-message \n make a signed message (Make sure to include your discord username in the signed message) \n After that, please SEND the block of signed message text here so we can verify your ownership of the account!", color=discord.Color.dark_grey())
                await channel.send(embed=embed)
            elif view.value == "Invite Whitelist":
                await channel.send('IW...')
            elif view.value == "Other Whitelist":
                await channel.send('OW...')
        elif view.value == "Staking":
            await channel.send('Stake? Well done or Medium Rare?')
            
            
        elif view.value == "Mod":
            await channel.send('Moderators will be with you shortly!')
            await channel.send("<@&947558052830249090>")
        elif view.value == "Staking Whitelist":
            embed = discord.Embed(title="In order to verify please go to this website ", description="Top 10", color=0x00ff00)
            embed=discord.Embed(description= "In order to verify please go to this website https://app.mycrypto.com/sign-message \n make a signed message (Make sure to include your discord username in the signed message) \n After that, please SEND the block of signed message text here so we can verify your ownership of the account!", color=discord.Color.dark_grey())
            await channel.send(embed=embed)
        elif view.value == "Invite Whitelist":
            await channel.send('IW...')
        elif view.value == "Other Whitelist":
            await channel.send('OW...')
        
        else:
            await channel.send('Cancelled...')

    else:
        await channel.send("dang, bad name.")

   
        
    

    
    
  





bot.run("OTM3MTU0NjUyNzcwODAzNzcy.YfXnSA.vlypBZcOPEy2ednav-HkTEwU7ns")