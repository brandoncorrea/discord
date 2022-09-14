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
  return before.status == discord.Status.offline and after.status != discord.Status.offline

def can_send_message(channel):
  return channel.permissions_for(channel.guild.me).send_messages

async def greet_member(member, channel):
  if member.name == 'ᴰᵉᵘᶜᵉˢ' and member.discriminator == '9928':
    await channel.send(f'{member.mention} Hey Daddy')
  elif member.display_name == 'ᴰᵉᵘᶜᵉˢ' and member.discriminator == '1066':
    await channel.send(f'{member.mention} Hey Bwawan')

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    for channel in after.guild.text_channels:
      if can_send_message(channel):
        await greet_member(after, channel)

client.run(TOKEN)

async def exit_gracefully(self, *args):
  await client.close()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)
