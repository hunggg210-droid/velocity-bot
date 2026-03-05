import discord
from discord.ext import commands

TOKEN = "MTQ3OTA1MzUzMDk4Njg0MDE0NQ.GhmEaS.ZbEHujws4oG7tOSmgRi33gF3TfNJ5wygdtKQfI"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot da online: {bot.user}")

@bot.command()
async def velocity(ctx):
    embed = discord.Embed(
        title="Roblox has updated!",
        description="Roblox has just updated! This version is now released and is being used by players!",
        color=0x2f3136
    )

    embed.add_field(
        name="Version",
        value="`version-d599f7fc52a8404c`",
        inline=False
    )

    embed.add_field(
        name="Platform",
        value="Windows",
        inline=True
    )

    embed.add_field(
        name="Download Here",
        value="[Download Link](https://rdd.whatexpsare.online/?channel=LIVE&binaryType=WindowsPlayer&version=version-d599f7fc52a8404c)",
        inline=True
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
