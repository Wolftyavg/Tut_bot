import discord
from discord.ext import commands

bots=commands.Bot(command_prefix='[')

@bots.event
async def onready():  #async 定義一個新東西
    print(">>Bot is online<<")

@bots.event
async def on_member_join(member):  #成員
    print(f'{member} join!')

@bots.event
async def on_member_remove(member):  #成員
    print(f'{member} leave!')


bots.run('OTgzNzA0NjMwNDY4OTY0NDUy.GbTITa.mB7c4lcde-9w-RUrP1s3qoeS6LEbk-nXZmeq-8') #貼上token