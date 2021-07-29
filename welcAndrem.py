import discord
from discord.ext import commands
import deloc

class Welcome(commands.Cog):
    "This command welcomes members"

    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(863482082625847359)
        embed = discord.Embed(title = f"Welcome {member} !!!", description = "Hope you have fun",colour=0xDC143C)
        await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        member = str(member)
        num = deloc.rem(member)
        if num == 0:
            channel = self.bot.get_channel(863482082625847359)
            embed = discord.Embed(title = f"Bye {member} hope you had fun!!!", description = "The userinfo of the departing member has been removed the database.",colour=0xDC143C)
            await channel.send(embed = embed)

def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))
