import os
import discord
import signal
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
  print(f'before status: {before.status}')
  print(f'after status: {after.status}')
  return before.status == discord.Status.offline and after.status != discord.Status.offline

def can_send_message(channel):
  print(f'channel.permissions_for(channel.guild.me).send_messages: {channel.permissions_for(channel.guild.me).send_messages}')
  return channel.permissions_for(channel.guild.me).send_messages

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    print(f'{after.nick or after.name} has come online!')
    for channel in after.guild.text_channels:
      print(f'looking at channel {channel}')
      if can_send_message(channel):
        print(f'sending message!')
        await channel.send(f'Hey there {after.nick or after.name}')

client.run(TOKEN)

async def exit_gracefully(self, *args):
  await client.close()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)
