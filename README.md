# discord

Sends messages to channels, tailored toward specific users, each time their online
status changes from `offline`.

### Run

`python3 ./dicaprio/bot.py`

### Test

`python3 ./dicaprio/bot_test.py`

### New Messages

Add new messages to `messages.json`. Specify the user with the format: `NAME#DISCRIMINATOR`,
where `NAME` is the user's username (not server name) and DISCRIMINATOR is the number after
the hash symbol.

Messages can *mention* the target user with the occurrence of `{mention}` somewhere
in the message.

### .env

Add a `.env` in the project directory with your discord token:

`DISCORD_TOKEN=#############`
