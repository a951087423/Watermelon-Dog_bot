from this import d
import discord
from discord.ext import commands
import json

with open("setting.json", mode = "r", encoding="utf8") as jfile:
    data = json.load(jfile)

bot = commands.Bot(data["Prefix"])



@bot.event
async def on_ready():
    print("目前登入身分：", bot.user)



@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")
@bot.command()
async def PING(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")



@bot.command()
async def 飯(ctx):
    pic = discord.File(data["pic_rice"])
    await ctx.send(file = pic)
@bot.command()
async def 可樂狗(ctx):
    pic = discord.File(data["pic_cola dog"])
    await ctx.send(file = pic)
@bot.command()
async def 美女(ctx):
    pic = discord.File(data["pic_zhan"])
    await ctx.send(file = pic)
@bot.command()
async def suck(ctx):
    pic = discord.File(data["pic_suck"])
    await ctx.send(file = pic)
@bot.command()
async def milk(ctx):
    pic = discord.File(data["pic_milk"])
    await ctx.send(file = pic)

@bot.command()
async def 拍拍(ctx):
    await ctx.send(data["url_paipai"])
@bot.command()
async def 菜狗(ctx):
    await ctx.send(data["url_caidog"])
@bot.command()
async def dinter(ctx):
    await ctx.send(data["url_dinter"])
@bot.command()
async def 看(ctx):
    await ctx.send(data["url_douyin_look"])
@bot.command()
async def 湯瑪士(ctx):
    await ctx.send(data["url_thomas_PainTrain"])
@bot.command()
async def JOJO(ctx):
    await ctx.send(data["url_JOJO_meme"])



bot.run(data["TOKEN"])