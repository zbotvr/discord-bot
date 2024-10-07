import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

bot.run('YOUR_DISCORD_BOT_TOKEN_HERE')
