import discord
from discord.ext import commands
import os

# create bot i b`nstance
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user} (ID: {bot.user.id})")
	print("------")
	
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# run the bot using the DISCORD_BOT_TOKEN environment variable

bot.run("MTQzNjg2MzAxMDM3ODQ4NTg3NA.GTQZKG.KZ_FVB7GUJOq_EnDEaPOshYM3ZxpbY3Vx5g2do")