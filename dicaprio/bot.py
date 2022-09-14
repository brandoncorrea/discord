import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

def has_joined(before, after):
  before.status == discord.Status.offline and after.status != discord.Status.offline

def can_send_message(channel):
  channel.permissions_for(channel.guild.me).send_messages

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    for channel in after.guild.text_channels:
      if can_send_message(channel):
        await channel.send(f'Hey there {after.nick or after.name}')

client.run(TOKEN)
