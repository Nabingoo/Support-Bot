import discord
from discord.ext import commands
from discord import Embed
import time
intents = discord.Intents.default()

intents.guilds = True
activity = discord.Activity(type=discord.ActivityType.watching, name="use ?mod to call a mod.")
bot = commands.Bot(command_prefix = "?", intents = intents,change_discord_methods=True, activity=activity, status=discord.Status.do_not_disturb)




@bot.command()
async def mod(ctx):  
    await ctx.channel.send('Moderators will be with you shortly!')
    await ctx.channel.send("<@&947558052830249090>")

class StakingOps(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

            
    @discord.ui.button(label='RADIO', style=discord.ButtonStyle.red)
    async def radiostake(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="How to Stake RADIO",description=  "Check out their Website! \n https://app.radioshack.org/stake \n For More help, Check out their Discord server! \n discord.gg/radioshack", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)
        self.value = "RADIO Staking"
          
    @discord.ui.button(label='USV', style=discord.ButtonStyle.blurple)
    async def usvstake(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="How to Stake USV", description= "Here's a Video to help! \n https://www.youtube.com/watch?v=scsrlyU0hz4 \n For More help, Check out their Discord server! \n discord.gg/usv", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)
        self.value = "USV Staking"
          
    @discord.ui.button(label='Get a Mod!', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        await (interaction.followup).send('A Mod will be with you shortly! \n <@&947558052830249090>', ephemeral=False)
        
        
        self.value = "Mod"
          
    
class Collabs(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
            
               
    @discord.ui.button(label='Whitelist Roles', style=discord.ButtonStyle.red)
    async def whitelistrole(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="Got it! We'll be in touch shortly", description="Please be patient.", color=discord.Color.dark_grey())
    
        await (interaction.followup).send(embed=embed, ephemeral=False)
        await (interaction.followup).send("<@568485392962158622>", ephemeral=False)
        self.value = "whiteroles"
          
    @discord.ui.button(label='Other Collab', style=discord.ButtonStyle.blurple)
    async def othercollab(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="We don't accept monetary/other collabs", description="We apologize for this inconvenience.", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)
        self.value = "othercollab"
          
    @discord.ui.button(label='Get a Mod!', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        await (interaction.followup).send('A Mod will be with you shortly! \n <@&947558052830249090>', ephemeral=False)
        
        
        self.value = "Mod"
          
class giveaways(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Did you win a giveaway?', style=discord.ButtonStyle.red)
    async def whitelistrole(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="Congrats!", description="Our giveaway team will be with you shortly.", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)
        await (interaction.followup).send("<@738340091457437706>")
        
        self.value = "winner"
          

class staff(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Do you want to join staff?', style=discord.ButtonStyle.red)
    async def whitelistrole(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="Sorry.", description="We aren't hiring at the moment, but we'll announce if we need more staff!", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)     
        self.value = "staff"
          
class WhitelistFunc(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Staking Whitelist', style=discord.ButtonStyle.green)
    async def stakewhite(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="In order to verify please go to this website ", description= " https://app.mycrypto.com/sign-message \n make a signed message (Make sure to include your discord username in the signed message) \n After that, please SEND the block of signed message text here so we can verify your ownership of the account!", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)       
        self.value = "Staking Whitelist"
             
          
    @discord.ui.button(label='Invite Whitelist', style=discord.ButtonStyle.green)
    async def invitewhite(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="For Invite Whitelists", description="Please do ?rank and ?invites \n \n Wait Patiently, thanks!", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False) 
        self.value = "Invite Whitelist"
          
    @discord.ui.button(label='Other Whitelist', style=discord.ButtonStyle.green)
    async def Whitelist(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        await (interaction.followup).send("A Staff member will be with you shortly. Please be patient", ephemeral=False) 
        self.value = "Other Whitelist"
          
    @discord.ui.button(label='Get a Mod!', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        await (interaction.followup).send('A Mod will be with you shortly! \n <@&947558052830249090>', ephemeral=False)
        
        
        self.value = "Mod"
          

class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

   
    @discord.ui.button(label='Whitelist', style=discord.ButtonStyle.green)
    async def Whitelist(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        view = WhitelistFunc()
        await (interaction.followup).send('What can we help you with today?', view=view)
        await view.wait()
        
        
        self.value = "Whitelist"
        
    @discord.ui.button(label='Staking', style=discord.ButtonStyle.green)
    async def Staking(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        
        view = StakingOps()
        await (interaction.followup).send('Here are the two Staking Options.', view=view, ephemeral = False)
        await view.wait()
        self.value = "Staking"
          
    @discord.ui.button(label='Get a Mod!', style=discord.ButtonStyle.green)
    async def GetaMod(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        await (interaction.followup).send('A Mod will be with you shortly! \n <@&947558052830249090>', ephemeral=False)
        
        
        self.value = "Mod"
          
    @discord.ui.button(label='Collabs', style=discord.ButtonStyle.blurple)
    async def collabs(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        view = Collabs()
        await (interaction.followup).send('We Offer Whitelist Roles in exchange for any sort of promotion/collaboration', view=view)
        await view.wait()
        self.value = "collab"
          
    @discord.ui.button(label='Giveaway', style=discord.ButtonStyle.blurple)
    async def giveaway(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        view = giveaways()
        await (interaction.followup).send('Giveaway Options!', view=view)
        await view.wait()
        
        self.value = "giveaway"
          
    @discord.ui.button(label='Joining Staff', style=discord.ButtonStyle.red)
    async def joinstaff(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        view = staff()
        await (interaction.followup).send('Interested about joining staff?', view=view)
        await view.wait()
        
        self.value = "JoinStaff"
          
    
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.response.send_message('Cancelling', ephemeral=True)
    
        self.value = "Cancel"
          

@bot.event
async def on_guild_channel_create(channel):
    time.sleep(1)
    if "ticket" in channel.name:
        view = Buttons()
        await channel.send('What can we help you with today?', view=view)
    
        await view.wait()
        
    else:
        await channel.send("dang, bad name.")



bot.run("OTM3MTU0NjUyNzcwODAzNzcy.YfXnSA.vlypBZcOPEy2ednav-HkTEwU7ns")