import json
import time
import discord
import requests
from discord.ext import commands
import aiohttp

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!')

SERVER_ID = 123456789  #Server with your bot
BOT_ID = 12345678  #Your bot ID
BOT_TOKEN = 'Your_Bot_Token' #Your Bot Token from discord applications
COINGEKO_API = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'


async def get_price():
    async with aiohttp.ClientSession() as session:
        async with session.get(COINGEKO_API) as response:
            if response.status == 200:
                price = await response.json()
                return 'BTC ' + str(price['bitcoin']['usd']) + ' $'
            else:
                return None


@bot.event
async def on_ready():
    print('Bot started')
    guild = bot.get_guild(SERVER_ID)
    member = guild.get_member(BOT_ID)
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$BTC'))
        price = await get_price()
        if price is None:
            time.sleep(30)
        else:
            await member.edit(nick=price)
        time.sleep(30)


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
