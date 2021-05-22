import discord as dc
import discord_slash as dcs
from decouple import config
import logging
from discord_slash.utils.manage_commands import create_option
#import backend

#---------------Logging---------------#
logger = logging.getLogger('discord')
logger.setLevel(logging.WARN)
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#---------------Defining Variables---------------#
client = dc.Client(intents=dc.Intents.all())
slash = dcs.SlashCommand(client, sync_commands=True)
try:
    guild_id = int(config("guild_id"))
    path_media = config("path_media")
except:
    print("Eine wichtige Variable wurde nicht gesetzt!\nBitte überprüfe deine Umgebungsvariablen!")
#---------------Shit that needs to be done---------------#
@client.event
async def on_ready():
    print("We are ready to rumble!")


#---------------The Commands---------------#
@slash.slash(name="Test", guild_ids=[guild_id], description="Ein einfacher Test")
async def test(ctx):
    await ctx.send(content="Der Test hat geklappt!")

@slash.slash(
        name="Hugs",
        description="Hug somebody",
        guild_ids=[guild_id],
        options=[
            create_option(
                name="person",
                description="The Person you wanna hug.",
                option_type=6,
                required=True
                )
            ]
        )
async def hug(ctx, person: str):
    await ctx.send(content=f"XY drückt dich!")

#---------------Don't you dare touch it!---------------#
client.run(config("token"))