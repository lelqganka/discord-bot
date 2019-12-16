import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='D')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)


@bot.command()
async def ping():
	await bot.say('ping_pong')
	await bot.say('You pinged me haha.')

	keep_alive()
bot.run('NjUyNDYzOTUwMjM0OTEwNzM1.Xeo7Ig.P6XyAnP01ySlJpy2VWVcw7ofNO4')
