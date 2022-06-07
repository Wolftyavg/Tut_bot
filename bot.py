import discord
from discord.ext import commands

bots=commands.Bot(command_prefix='[')

@bots.event
async def onready():  #async 定義一個新東西
    print(">>Bot is online<<")

bots.run('OTgzNzA0NjMwNDY4OTY0NDUy.G33fCz.ZnLuVARocx-VNxWPI-VAoxZPv0OIkCdRaDIBA4') #貼上token