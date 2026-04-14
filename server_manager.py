from discord.ext import commands

class ServerManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def listservers(self, ctx):
        """Listet alle Server auf."""
        # Wir listen einfach alle Namen auf
        guild_names = [g.name for g in self.bot.guilds]
        await ctx.send(f"Ich bin auf diesen Servern: {', '.join(guild_names)}")

    @commands.command()
    async def leaveserver(self, ctx, id: int):
        """Verlässt einen Server anhand der ID."""
        guild = self.bot.get_guild(id)
        if guild:
            await guild.leave()
            await ctx.send(f"Erfolgreich verlassen: {guild.name}")
        else:
            await ctx.send("Server nicht gefunden.")

async def setup(bot):
    await bot.add_cog(ServerManager(bot))
