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

        roles = []
        if user==None:
            user=ctx.author
        for role in user.roles:
            roles.append(str(role.mention))

        roles.reverse()

        embed=discord.Embed(title=f":boy: 使用者資訊 - {user}", description="‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", color=0x2f56ee, timestamp = datetime.datetime.utcnow())
        embed.set_thumbnail(url=user.avatar_url),
        embed.set_author(name="[開發中] 西瓜狗狗", icon_url="https://i.imgur.com/MLVO5sl.jpg")
        embed.add_field(name=":mag_right: 名稱", value=user.display_name, inline=True)
        embed.add_field(name=":id: Discord ID", value=user.id, inline=True)
        embed.add_field(name="‎", value="‎", inline=False)
        embed.add_field(name=":calendar_spiral: 創建Discord帳號於", value=user.created_at, inline=False)
        embed.add_field(name=":calendar_spiral: 加入此伺服器於", value=user.joined_at, inline=False)
        embed.add_field(name="‎", value="‎", inline=False)
        if len(str(" | ".join([x.mention for x in user.roles]))) > 1024:
            embed.add_field(name=f":crown: 身份組 [{len(user.roles)}]", value="滿出來了！", inline=False)
        else:
            embed.add_field(name=f":crown: 身份組 [{len(user.roles)}]", value=" | ".join(roles), inline=False)

        embed.set_footer(text=f" {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    async def 聊天(self, ctx, user:discord.Member=None):
        embed=discord.Embed(title=":white_check_mark: 列表：", description=":warning: 註：以下為 和機器人的聊天字元 不須加入前綴  \" ~ \"  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", color=0x58ef2e, timestamp = datetime.datetime.utcnow())
        embed.set_author(name="聊天指令", icon_url="https://i.imgur.com/V4AdcL7.png")
        embed.set_thumbnail(url="https://i.imgur.com/RTrXluI.jpg")
        embed.add_field(name="1.  法鬥", value="‎", inline=False)
        embed.add_field(name="2.  6", value="‎", inline=False)
        embed.add_field(name="3.  你 / 妳", value="‎", inline=False)
        embed.add_field(name="4.  賴", value="‎", inline=False)
        embed.add_field(name="5.  豬 / 黃文言 / 文言", value="‎", inline=False)
        embed.add_field(name="6.  龍共", value="‎", inline=False)
        embed.set_footer(text=f" {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(指令(bot))

