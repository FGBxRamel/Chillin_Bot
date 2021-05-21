import discord as dc
import discord_slash as dc_s
from decouple import config
import logging
#import backend

logger = logging.getLogger('discord')
logger.setLevel(logging.WARN)
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = dc.Client(intents=dc.Intents.all())
slash = dc_s.SlashCommand(client, sync_commands=True)
guild_id = int(config("guild_id"))

@client.event
async def on_ready():
    print("We are ready to rumbble!")

@slash.slash(name="test", guild_ids=[guild_id], description="Ein einfacher Test")
async def test(ctx):
    await ctx.send(content="Der Test hat geklappt!")


client.run(config("token"))