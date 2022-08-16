import discord
from discord.ext import commands
from .core.classes import Cog_Extension

class 指令(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")
    @commands.command()
    async def PING(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")
    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f"重新載入 {extension} 完成！！")



def setup(bot):
    bot.add_cog(指令(bot))

