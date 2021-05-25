import discord as dc
import discord_slash as dcs
from decouple import config
import logging
from discord_slash.utils.manage_commands import create_option
import random as rd
import os
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
    if not path_media.endswith("/"):
        path_media += "/"
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
async def hug(ctx, person):
    hug_embed = dc.Embed(
                    title="Cuddle Attack!",
                    description="Das ist sehr effektiv!",
                    color=rd.randint(0, 0xFFFFFF)
                ).set_author(name=ctx.author.display_name)
    hug_file = dc.File(random_image("hugs"), filename="hug.jpg")
    hug_embed.set_image(url="attachment://hug.jpg")
    await ctx.send(content=f"Hey {person.mention}! Du wirst gedrückt:", embed=hug_embed, file=hug_file)

@slash.slash(
        name="Kiss",
        description="Give someone a kiss",
        guild_ids=[guild_id],
        options=[
            create_option(
                name="person",
                description="The Person you wanna kiss.",
                option_type=6,
                required=True
                )
            ]
        )
async def kiss(ctx, person):
    kiss_embed = dc.Embed(
                    title="Kiss",
                    description="*Knutsch*",
                    color=rd.randint(0, 0xFFFFFF)
                ).set_author(name=ctx.author.display_name)
    kiss_file = dc.File(random_image("kiss"), filename="kiss.jpg")
    kiss_embed.set_image(url="attachment://kiss.jpg")
    await ctx.send(content=f"Hey {person.mention}! Dir wurde ein Kuss gegeben:", embed=kiss_embed, file=kiss_file)


#---------------Functions---------------#
def random_image(type, path=config("path_media")):
    if not path.endswith("/" or "\\"):
        path += "/"
    return (path_media + type + "/" + str(rd.choice(os.listdir(path_media + type))))


#---------------Don't you dare touch it!---------------#
client.run(config("token"))