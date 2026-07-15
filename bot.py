import discord
from discord.ext import commands

from config import TOKEN


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None,
)


@bot.event
async def on_ready():
    print("-" * 40)
    print(f"Logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print("Bot is ready.")
    print("-" * 40)

    await bot.change_presence(
        activity=discord.Game("Starting up...")
    )


if __name__ == "__main__":
    bot.run(TOKEN)