import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class ServerManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def listservers(self, ctx):
        """Listet alle Server auf, auf denen der Bot ist."""
        msg = "### 🖥️ Verbundene Server:\n"
        for guild in self.bot.guilds:
            msg += f"• **{guild.name}** | ID: `{guild.id}`\n"
        
        await ctx.send(msg if len(msg) < 2000 else "Liste zu lang.")

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def leaveserver(self, ctx, guild_id: int):
        """Lässt den Bot einen Server verlassen."""
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return await ctx.send("❌ Server-ID nicht gefunden.")
        
        await guild.leave()
        await ctx.send(f"✅ Bot hat **{guild.name}** verlassen.")

async def setup(bot):
    await bot.add_cog(ServerManager(bot))
