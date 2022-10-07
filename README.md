# GasCalcutor

Those discord bots tracks $BTC, $ETH, $SOL prices in real time using CoinGeko free API. ETH bot also checks current GAS and SOL bot checks current TPS.
![](https://cdn.discordapp.com/attachments/607052288842006534/1027935743638769794/CryptoTracker.png)

These bots don't need any permissions other than "change nickname", so it's perfectly safe to use them (don't give them any extra permissions and nothing will happen).

Also if you don't want to run bots by yourself you can use these links to add them to your servers!

[BTC Bot](https://discord.com/api/oauth2/authorize?client_id=1027660647565111358&permissions=67108864&scope=bot)  |  [ETH Bot](https://discord.com/api/oauth2/authorize?client_id=1027570717107167242&permissions=67108864&scope=bot)  |  [SOL Bot](https://discord.com/api/oauth2/authorize?client_id=1027678339684638771&permissions=67108864&scope=bot)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements from requirements.txt.

```bash
pip install -r requirements.txt
```

## Usage

Firstly you need to create discord bot, [here](https://discordpy.readthedocs.io/en/stable/discord.html) is guide.

Secondly you need to change this constants (in all bots).

```python
SERVER_ID = 123456789  #Server with your bot
BOT_ID = 12345678  #Your bot ID
BOT_TOKEN = 'Your_Bot_Token' #Your Bot Token from discord applications
ETHERSCAN_API = 'Your API key'  #Etherscan API key (only for eth tracker)
```

[Here](https://etherscan.io/apis) you can get Etherscan API key (free one is enough).

You don't need to change next constants!
```
SOL_RPC = 'https://api.mainnet-beta.solana.com/' #Used in Solana tracker
COINGEKO_API = 'https://api.coingecko.com/api/v3/simple/price? ids=solana&vs_currencies=usd' #used in all trackers
```
Then run this commands.
```
python BTC_Tracker.py
python ETH_Tracker.py
python SOL_Tracker.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)