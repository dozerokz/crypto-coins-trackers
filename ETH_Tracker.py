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
ETHERSCAN_API = 'Your API key'  #Etherscan API key (only for eth tracker)
COINGEKO_API = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'

url_params = {
    'module': 'gastracker',
    'action': 'gasoracle',
    'apikey': ETHERSCAN_API
}


async def get_price():
    async with aiohttp.ClientSession() as session:
        async with session.get(COINGEKO_API) as response:
            if response.status == 200:
                price = await response.json()
                return 'ETH ' + str(price['ethereum']['usd']) + ' $'
            else:
                return None


async def get_gas():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.etherscan.io/api', params=url_params) as response:
            if response.status == 200:
                response_parsed = await response.json()
                result = response_parsed['result']
                return '⚡️' + result['FastGasPrice'] + ' |🚶' + result['ProposeGasPrice'] + ' |🐢' + result['FastGasPrice']
            else:
                return None


@bot.event
async def on_ready():
    print('Bot started')
    guild = bot.get_guild(SERVER_ID)
    member = guild.get_member(BOT_ID)
    while True:
        try:
            price = await get_price()
            gas = await get_gas()

            if price is None:
                time.sleep(30)
            else:
                await member.edit(nick=price)
            if gas is None:
                time.sleep(30)
            else:
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=gas))
            time.sleep(30)
        except:
            time.sleep(30)


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
