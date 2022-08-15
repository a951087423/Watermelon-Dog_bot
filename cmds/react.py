from lib2to3.refactor import RefactoringTool
import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json

with open("setting.json", mode = "r", encoding="utf8") as jfile:
    data = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def rice(self, ctx):
        pic = discord.File(data["pic_rice"])
        await ctx.send(file = pic)
    @commands.command()
    async def 可樂狗(self, ctx):
        pic = discord.File(data["pic_cola dog"])
        await ctx.send(file = pic)
    @commands.command()
    async def 美女(self, ctx):
        pic = discord.File(data["pic_zhan"])
        await ctx.send(file = pic)
    @commands.command()
    async def suck(self, ctx):
        pic = discord.File(data["pic_suck"])
        await ctx.send(file = pic)
    @commands.command()
    async def milk(self, ctx):
        pic = discord.File(data["pic_milk"])
        await ctx.send(file = pic)

    @commands.command()
    async def 拍拍(self, ctx):
        await ctx.send(data["url_paipai"])
    @commands.command()
    async def 菜狗(self, ctx):
        await ctx.send(data["url_caidog"])
    @commands.command()
    async def dinter(self, ctx):
        await ctx.send(data["url_dinter"])
    @commands.command()
    async def 看(self, ctx):
        await ctx.send(data["url_douyin_look"])
    @commands.command()
    async def 湯瑪士(self, ctx):
        await ctx.send(data["url_thomas_PainTrain"])
    @commands.command()
    async def JOJO(self, ctx):
        await ctx.send(data["url_JOJO_meme"])


def setup(bot):
    bot.add_cog(React(bot))

