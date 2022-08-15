import imp
import discord
from discord.ext import commands
from .core.classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ["你", "妳"]
        if msg.content in keyword:
            await msg.channel.send("<@561191499442946049> 你！！")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "法鬥":
            await msg.channel.send("你又怎樣？")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "賴":
            await msg.channel.send("<@652094533982748683> 我有大！要不要飛！ \n倒了倒了倒了！\n我拉補我拉補我拉補！")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "6" and msg.author != self.bot.user:
            await msg.channel.send("6")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "豬":
            await msg.channel.send("<@581704499945799691>")



def setup(bot):
    bot.add_cog(Event(bot))

