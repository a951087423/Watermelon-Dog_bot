from ast import keyword
from this import d
import discord
from discord.ext import commands
from .core.classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "法鬥":
            await msg.channel.send("你又怎樣")
        if msg.content == "6" and msg.author != self.bot.user:
            await msg.channel.send("6")
        keyword = ["你", "妳"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("<@561191499442946049> 你！！")
        if msg.content == "賴":
            await msg.channel.send("<@652094533982748683>\n我有大！要不要飛！要不要飛！\n倒了 倒了！\n我拉補 我拉補 我拉補！")
        keyword = ["豬", "黃文言", "文言"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("<@581704499945799691> 豬")










def setup(bot):
    bot.add_cog(Event(bot))

