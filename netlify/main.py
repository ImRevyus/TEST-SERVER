import os
import requests
import discord
import keep_alive
from discord.ext import commands

keep_alive.keep_alive()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command()
async def check(ctx, coin: str):
    api_key = "V1DSJ3XTBYJ20WI4NG0U"
    api_url = f"https://api.cryptowat.ch/markets/binance/{coin}usdt/price?apikey={api_key}"
    response = requests.get(api_url)

    if response.status_code == 200:
        price = response.json()["result"]["price"]
        await ctx.send(f"The price of {coin} is {price:.2f} USDT")
    else:
        await ctx.send("Error retrieving price data")

bot.run(os.environ["Token"])