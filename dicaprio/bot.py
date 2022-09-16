import os
import json
import discord
import signal
import random
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
  
# Opening JSON file
f = open(f'{os.path.dirname(os.path.realpath(__file__))}/messages.json')
message_formats = json.load(f)
f.close()

def messages_for(member):
  id = f'{member.name}#{member.discriminator}'
  if id in message_formats:
    return message_formats[id]

async def greet_member(member, channel):
  messages = messages_for(member)
  if messages:
    await channel.send(random.choice(messages).format(mention=member.mention))

def has_joined(before, after):
  return before.status == discord.Status.offline and after.status != discord.Status.offline

def can_send_message(member, channel):
  return channel.permissions_for(member).send_messages

def should_greet(member, channel):
  r4_url = 'https://discord.com/channels/976337221663723521/1000437303870750801'
  return r4_url == channel.jump_url and can_send_message(channel.guild.me, channel) and can_send_message(member, channel)

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    for channel in after.guild.text_channels:
      if should_greet(after, channel):
        await greet_member(after, channel)

async def exit_gracefully(self, *args):
  await client.close()

if __name__ == '__main__':
  client.run(TOKEN)
  signal.signal(signal.SIGINT, exit_gracefully)
  signal.signal(signal.SIGTERM, exit_gracefully)
