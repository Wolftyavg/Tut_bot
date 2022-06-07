import discord
from discord.ext import commands

bots=commands.Bot(command_prefix='[')

@bot.event
async def onready():  #async 定義一個新東西
    print(">>Bot is online<<")

bots.run()