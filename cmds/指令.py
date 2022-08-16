from msilib.schema import Icon
from sqlite3 import Timestamp
import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import datetime

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
        await ctx.send(f"重新載入 >>{extension}<< 完成！！")
    @commands.command()
    async def userinfo(self, ctx, user:discord.Member=None):

        if user==None:
            user=ctx.author

        embed=discord.Embed(title=f"UserInfo - {user}", description="‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", color=0x2f56ee, timestamp = datetime.datetime.utcnow())
        embed.set_thumbnail(url=user.avatar_url),
        embed.set_author(name=ctx.message.author.name, icon_url=user.avatar_url)
        embed.add_field(name="Name", value=user.display_name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="‎", value="-", inline=False)
        embed.add_field(name="Created Discord Account", value=user.created_at, inline=False)
        embed.add_field(name="Joined this server", value=user.joined_at, inline=False)
        embed.add_field(name="‎", value="-", inline=False)
        embed.set_footer(text=f" {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @commands.command()
    async def 聊天(self, ctx):
        embed=discord.Embed(title="列表：", description="註：以下為與機器人聊天指令 不須加入前綴  ~  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", color=0x58ef2e, timestamp = datetime.datetime.utcnow())
        embed.set_author(name="聊天指令", icon_url="https://i.imgur.com/V4AdcL7.png")
        embed.set_thumbnail(url="https://i.imgur.com/RTrXluI.jpg")
        embed.add_field(name="1.  法鬥", value="-", inline=False)
        embed.add_field(name="2.  6", value="-", inline=False)
        embed.add_field(name="3.  你, 妳", value="-", inline=False)
        embed.add_field(name="4.  賴", value="-", inline=False)
        embed.add_field(name="5.  豬, 黃文言, 文言", value="-", inline=False)
        embed.add_field(name="6.  龍共", value="-", inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(指令(bot))

