import requests
import json
import time
import discord
import requests
from discord.ext import commands
import aiohttp

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!')

SERVER_ID = 123456789
BOT_ID = 123456789
BOT_TOKEN = 'your_bot_token'
SOL_RPC = 'https://api.mainnet-beta.solana.com/'
COINGEKO_API = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'

json_data = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'getRecentPerformanceSamples',
    'params': [
        1,
    ],
}


async def get_price():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(COINGEKO_API) as response:
                if response.status == 200:
                    price = await response.json()
                    return 'SOL ' + str(price['solana']['usd']) + ' $'
                else:
                    return None
    except: pass

async def get_tps():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(SOL_RPC, json=json_data) as response:
                if response.status == 200:
                    result = await response.json()
                    result = result['result'][0]
                    numTransactions = result['numTransactions']
                    samplePeriodSecs = result['samplePeriodSecs']
                    if samplePeriodSecs == 0:
                        return 'TPS: 0'
                    else:
                        return 'TPS: ' + str(round(float(numTransactions)/float(samplePeriodSecs)))
                else:
                    return None
    except: pass


@bot.event
async def on_ready():
    print('Bot started')
    guild = bot.get_guild(SERVER_ID)
    member = guild.get_member(BOT_ID)
    while True:
        price = await get_price()
        tps = await get_tps()
        print(price)

        if price is None:
            time.sleep(30)
        else:
            await member.edit(nick=price)
        if tps is None:
            time.sleep(30)
        else:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=tps))
        time.sleep(30)

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
