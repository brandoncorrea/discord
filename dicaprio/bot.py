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

def can_send_message(member, channel):
  return channel.permissions_for(member).send_messages

async def greet_member(member, channel):
  if member.name == 'ᴰᵉᵘᶜᵉˢ' and member.discriminator == '9928':
    await channel.send(f'{member.mention} Hey Daddy 😘')
  elif member.display_name == 'jazfunk' and member.discriminator == '6114':
    await channel.send(f'{member.mention} Ew what even!? 🍵')
  elif member.display_name == 'jules' and member.discriminator == '3901':
    await channel.send(f'{member.mention} Bang 💎')

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    for channel in after.guild.text_channels:
      if can_send_message(channel.guild.me, channel) and can_send_message(after, channel):
        await greet_member(after, channel)

client.run(TOKEN)

async def exit_gracefully(self, *args):
  await client.close()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)
