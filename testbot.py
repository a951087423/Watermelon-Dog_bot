from this import d
from unicodedata import name
import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.all()

with open("setting.json", mode = "r", encoding="utf8") as jfile:
    data = json.load(jfile)



bot = commands.Bot(data["Prefix"], intents = intents)



@bot.event
async def on_ready():
    print("目前登入身分：", bot.user)



@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"重新載入 {extension} 完成！！")



for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")



if __name__ == "__main__":
    bot.run(data["TOKEN"])