import os
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

def has_joined(before, after):
  return before.status == discord.Status.offline and after.status != discord.Status.offline

def can_send_message(member, channel):
  return channel.permissions_for(member).send_messages

def random_ryan_message(member):
  messages = [
    f"{member.mention} The only respectable thing about you, old sport, is your money.",
    f"{member.mention} Did my heart love 'til now? Forswear its sight. For I never saw true beauty 'til this night.",
    f"{member.mention} Be Thankful for the noobs, for they have made you.",
    f"{member.mention} had my curiosity... but now he has my attention.",
    f"{member.mention} Give me my sin again.",
    f"{member.mention} I’m having a birthday party but you’re not invited, but you can come if you want.",
    f"{member.mention} Is it possible to improve on perfection?"
  ]
  return random.choice(messages)

def random_shhourti_message(member):
  messages = [
    f"{member.mention} Shhourti's like a melody in my head that I can't keep out.",
    f"{member.mention} You got them Apple Bottom jeans and boots with the fur?",
    f"{member.mention} Somebody call 9-1-1, Shhourti fire burning on the dance floor!",
    f"{member.mention} I should be playing in the winter snow, but I’mma be under the mistletoe with Shhourti."
  ]
  return random.choice(messages)

def random_jules_message(member):
  messages = [
    f"{member.mention} Bang 💎",
    f"{member.mention} Hello NOT real Bwawan",
    f"{member.mention} Oh look guys, is a noob betrayer 😒",
    f"Eject {member.mention}, she's the the imposter!",
    f"{member.mention} انا احب الجميع لكنك",
    f"{member.mention} You ROCK! 🪨 Hah. Get it? Cause jewels are like... nevermind."
  ]
  return random.choice(messages)

def random_matcha_message(member):
  messages = [
    f"{member.mention} Ew what even!? 🍵",
    f"{member.mention} coffee is WAY better ☕",
    f"{member.mention} so are you like, liquid pot or something?",
    f"{member.mention} what's the latest Tic-Tac trend these days?"
  ]
  return random.choice(messages)

def random_deuces_message(member):
  messages = [
    f"{member.mention} Hey Daddy 😘"
  ]
  return random.choice(messages)

def random_ssmonk_message(member):
  messages = [
    f'{member.mention} Hey sexy 😉'
  ]
  return random.choice(messages)

async def greet_member(member, channel):
  if member.name == 'ᴰᵉᵘᶜᵉˢ' and member.discriminator == '9928':
    await channel.send(random_deuces_message(member))
  elif member.name == 'jazfunk' and member.discriminator == '6114':
    await channel.send(random_matcha_message(member))
  elif member.name == 'jules' and member.discriminator == '3901':
    await channel.send(random_jules_message(member))
  elif member.name == 'Hira' and member.discriminator == '2710':
    await channel.send(random_ryan_message(member))
  elif member.name == 'shhourti' and member.discriminator == '6292':
    await channel.send(random_shhourti_message(member))
  elif member.name == 'A_ssmonk' and member.discriminator == '0763':
    await channel.send(random_ssmonk_message(member))

def should_greet(member, channel):
  r4_url = 'https://discord.com/channels/976337221663723521/1000437303870750801'
  return r4_url == channel.jump_url and can_send_message(channel.guild.me, channel) and can_send_message(member, channel)

@client.event
async def on_presence_update(before, after):
  if has_joined(before, after):
    for channel in after.guild.text_channels:
      if should_greet(after, channel):
        await greet_member(after, channel)

client.run(TOKEN)

async def exit_gracefully(self, *args):
  await client.close()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)
