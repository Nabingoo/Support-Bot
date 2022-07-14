import discord
from discord.ext import commands
from discord import Embed
import time
intents = discord.Intents.default()

intents.guilds = True

bot = commands.Bot(command_prefix = ";", intents = intents,change_discord_methods=True)

class StakingOps(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='RADIO', style=discord.ButtonStyle.red)
    async def radiostake(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "RADIO Staking"
        self.stop()
    @discord.ui.button(label='USV', style=discord.ButtonStyle.blurple)
    async def usvstake(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "USV Staking"
        self.stop()
    
class Collabs(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Whitelist Roles', style=discord.ButtonStyle.red)
    async def whitelistrole(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "whiteroles"
        self.stop()
    @discord.ui.button(label='Other Collab', style=discord.ButtonStyle.blurple)
    async def othercollab(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        self.value = "othercollab"
        self.stop()
    

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
    @discord.ui.button(label='Collabs', style=discord.ButtonStyle.blurple)
    async def collabs(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Working', ephemeral=True)
        
        self.value = "collab"
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
                embed = discord.Embed(title="In order to verify please go to this website ", description= " https://app.mycrypto.com/sign-message \n make a signed message (Make sure to include your discord username in the signed message) \n After that, please SEND the block of signed message text here so we can verify your ownership of the account!", color=discord.Color.dark_grey())
                await channel.send(embed=embed)
                
            elif view.value == "Invite Whitelist":
                await channel.send('IW...')
            elif view.value == "Other Whitelist":
                await channel.send('OW...')
        elif view.value == "Staking":
            view = StakingOps()
            await channel.send('Here are the two Staking Options.', view=view)
            await view.wait()

            if view.value == "USV Staking":
                embed = discord.Embed(title="How to Stake USV", description= "Here's a Video to help! \n https://www.youtube.com/watch?v=scsrlyU0hz4 \n For More help, Check out their Discord server! \n discord.gg/usv", color=discord.Color.dark_grey())
                
                await channel.send(embed=embed)
            elif view.value == "RADIO Staking":
                embed = discord.Embed(title="How to Stake RADIO",description=  "Check out their Website! \n https://app.radioshack.org/stake \n For More help, Check out their Discord server! \n discord.gg/radioshack", color=discord.Color.dark_grey())
             
                await channel.send(embed=embed)
            
        elif view.value == "Mod":
            await channel.send('Moderators will be with you shortly!')
            await channel.send("<@&947558052830249090>")
        elif view.value == "collab":
            view = Collabs()
            await channel.send('We Offer Whitelist Roles in exchange for any sort of promotion/collaboration', view=view)
            await view.wait()

            if view.value == "whiteroles":
                embed = discord.Embed(title="Got it! We'll be in touch shortly", description="Please be patient.", color=discord.Color.dark_grey())
                
                await channel.send(embed=embed)
                await channel.send("<@568485392962158622>")
            elif view.value == "othercollab":
                embed = discord.Embed(title="We don't accept monetary/other collabs", description="We apologize for this inconvenience.", color=discord.Color.dark_grey())
                
                await channel.send(embed=embed)
        
        else:
            await channel.send('Cancelled...')

    else:
        await channel.send("dang, bad name.")

   
        
    

    
    
  





bot.run("OTM3MTU0NjUyNzcwODAzNzcy.YfXnSA.vlypBZcOPEy2ednav-HkTEwU7ns")