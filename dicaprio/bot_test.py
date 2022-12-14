import unittest
import asynctest
from bot import messages_for, greet_member

class Member:
  def __init__(self, name, discriminator, mention):
    self.name = name
    self.discriminator = discriminator
    self.mention = mention

class Channel:
  def __init__(self):
    self.sent_message = False
    self.message = None

  async def send(self, message):
    self.sent_message = True
    self.message = message

fake_user = Member('garbage', '0123', 'Imposter!!!')
bub = Member('¯\_(ツ)_/¯', '3216', 'Bub')
ssmonk = Member('A_ssmonk', '0763', 'ssmonk')
deuces = Member('ᴰᵉᵘᶜᵉˢ', '9928', 'Papi')
matcha = Member('jazfunk', '6114', 'matcha')
jules = Member('jules', '3901', 'Kok')
brit = Member('shhourti', '6292', 'Brit')
ryan = Member('Hira', '2710', 'Ryan')
godfather = Member('Godfather_Actual', '7430', 'Godfather')
presy = Member('PreZzz', '7543', 'Presy')
yoda = Member('GunProBambi', '6809', 'Yoda')

class TestBotMethods(unittest.TestCase):

  def test_messages_for_none(self):
    messages = messages_for(fake_user)
    self.assertEqual(True, not messages)

  def test_messages_for_bub(self):
    messages = messages_for(bub)
    expected_messages = ['{mention} игнорирование']
    self.assertEqual(messages, expected_messages)

  def test_messages_for_ssmonk(self):
    messages = messages_for(ssmonk)
    expected_messages = ['{mention} Hey sexy 😉']
    self.assertEqual(messages, expected_messages)

  def test_messages_for_deuces(self):
    messages = messages_for(deuces)
    expected_messages = [
      '{mention} Hey Daddy 😘', 
      '{mention} Hola Papi 😍'
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_matcha(self):
    messages = messages_for(matcha)
    expected_messages = [
      "{mention} Ew what even!? 🍵",
      "{mention} coffee is WAY better ☕",
      "{mention} so are you like, liquid pot or something?",
      "{mention} what's the latest Tic-Tac trend these days?"
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_jules(self):
    messages = messages_for(jules)
    expected_messages = [
      "{mention} Bang 💎",
      "{mention} Hello NOT real Bwawan",
      "{mention} Oh look guys, is a noob betrayer 😒",
      "Eject {mention}, she's the the imposter!",
      "{mention} انا احب الجميع لكنك",
      "{mention} You ROCK! 🪨 Hah. Get it? Cause jewels are like... nevermind."
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_brit(self):
    messages = messages_for(brit)
    expected_messages = [
      "{mention} Shhourti's like a melody in my head that I can't keep out.",
      "{mention} You got them Apple Bottom jeans and boots with the fur?",
      "{mention} Somebody call 9-1-1, Shhourti fire burning on the dance floor!",
      "{mention} I should be playing in the winter snow, but I’mma be under the mistletoe with Shhourti."
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_ryan(self):
    messages = messages_for(ryan)
    expected_messages = [
      "{mention} The only respectable thing about you, old sport, is your money.",
      "{mention} Did my heart love 'til now? Forswear its sight. For I never saw true beauty 'til this night.",
      "{mention} Be Thankful for the noobs, for they have made you.",
      "{mention} had my curiosity... but now he has my attention.",
      "{mention} Give me my sin again.",
      "{mention} I’m having a birthday party but you’re not invited, but you can come if you want.",
      "{mention} Is it possible to improve on perfection?",
      "{mention} 'Tis an honor, Lord Ryab XVIII (the coolest one)"
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_godfather(self):
    messages = messages_for(godfather)
    expected_messages = [
      '{mention} Father...? 🥹'
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_presy(self):
    messages = messages_for(presy)
    expected_messages = [
      'Greetings, {mention} 🖖'
    ]
    self.assertEqual(messages, expected_messages)

  def test_messages_for_yoda(self):
    messages = messages_for(yoda)
    expected_messages = [
      '{mention} Hello there',
      '{mention} Yo yo yo yo Yoda',
      '{mention} I have waited a long time for this moment, my little green friend.',
      "{mention} I must know the truth, Master."
    ]
    self.assertEqual(messages, expected_messages)


class TestAsyncBotMethods(asynctest.TestCase):
  async def test_greet_nobody(self):
    channel = Channel()
    await greet_member(fake_user, channel)
    self.assertEqual(False, channel.sent_message)

  async def test_greet_ryan(self):
    channel = Channel()
    ryan_messages = [
      "Ryan The only respectable thing about you, old sport, is your money.",
      "Ryan Did my heart love 'til now? Forswear its sight. For I never saw true beauty 'til this night.",
      "Ryan Be Thankful for the noobs, for they have made you.",
      "Ryan had my curiosity... but now he has my attention.",
      "Ryan Give me my sin again.",
      "Ryan I’m having a birthday party but you’re not invited, but you can come if you want.",
      "Ryan Is it possible to improve on perfection?",
      "Ryan 'Tis an honor, Lord Ryab XVIII (the coolest one)"
    ]
    await greet_member(ryan, channel)
    self.assertEqual(True, channel.sent_message)
    self.assertEqual(True, channel.message in ryan_messages)


if __name__ == '__main__':
  unittest.main()