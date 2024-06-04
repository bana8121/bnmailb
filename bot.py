from config import TOKEN
import flask
import discord
from discord.ext import commands
import asyncio
import time

allowed_users = [1052209380596125776]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
app = flask.Flask(__name__)

@bot.event
async def on_ready():
    print(bot.user.name)
    print("준비 완!")

@bot.command(name="goauth")
async def restricted_command(ctx):
    if ctx.author.id in allowed_users:
        await ctx.send(f'hello {ctx.author.name}making auth in 3 seconds, plz wait :) (인증기를 3초안에 만듭니다, 기다려주세요)')
        time.sleep(3)
        ctx.sned
    else:
        await ctx.send('no permission, sorry. (권한이 없습니다, 죄송합니다)')

    bot.run(TOKEN)