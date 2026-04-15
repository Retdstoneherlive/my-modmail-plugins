from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class ServerManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def listservers(self, ctx):
        """Listet alle Server auf."""
        guilds = [f"• {g.name} (ID: `{g.id}`)" for g in self.bot.guilds]
        output = "### 🖥️ Verbundene Server:\n" + "\n".join(guilds)
        await ctx.send(output[:2000])

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def leaveserver(self, ctx, guild_id: int):
        """Verlässt einen Server via ID."""
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return await ctx.send("❌ Server-ID nicht gefunden.")
        await guild.leave()
        await ctx.send(f"✅ Bot hat **{guild.name}** verlassen.")

async def setup(bot):
    await bot.add_cog(ServerManager(bot))
