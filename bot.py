# main.py
import discord
from discord.ext import commands
import json
import asyncio
from scrapybara import Scrapybara

class VirtualPCBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        super().__init__(command_prefix="!", intents=intents)
        
        # Load config
        with open("config/config.json", "r") as f:
            self.config = json.load(f)
        
        # Initialize Scrapybara
        self.scrapybara = Scrapybara(api_key=self.config["scrapybara_api_key"])
        
    async def setup_hook(self):
        await self.load_extension("cogs.virtual_pc")

async def main():
    bot = VirtualPCBot()
    async with bot:
        await bot.start(bot.config["discord_token"])

if __name__ == "__main__":
    asyncio.run(main())
