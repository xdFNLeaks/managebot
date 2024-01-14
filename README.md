# managebot

**Version 1.0.2 has been released!**

just a little project i'm working on that allows you to view and manage your docker containers from discord.

---

### What's New? *(v1.0.2)*

- Added Auto Update when restarting/starting. [Check here to see how to enable it!](https://github.com/xdFNLeaks/managebot/tree/v1.0.2?tab=readme-ov-file#this-script-is-to-run-managebot-that-updates-itself-at-each-restartrun-recommended)
- Added delete to `/docker execute`

---

### Features

- Executing Docker Commands (`/docker execute`) (start, stop, restart, pause, unpause)
- Listing all docker containers and sorts them into Online & Offline. (`/list`)
- Docker Image Management + Image Pruning (`/docker images` | `/docker prune`)

### Planned Features

- Web Interface (possibly, not 100% sure if I can make this right now)

---

## Installation

**You must have Docker & Python installed and running.**

To run this, first clone this repository:

```
sudo git clone https://github.com/xdFNLeaks/managebot.git
```

**After you have cloned this repo, open `config.json` and edit it to your liking.**
- `token` = Your discord bot token. ([Discord Developer Portal](https://discord.com/developers/applications))
- `timezone_offset` = Your timezone offset. ([List of UTC offsets - Wikipedia](https://en.wikipedia.org/wiki/List_of_UTC_offsets))
- `guild_ids` = Your server ID. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `allowed_user_ids` = The ID of the bot admin. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `type` = The Rich Presence type (Playing ..., Watching ...) - Currently available: Playing, Watching, Listening.
- `message` = The message that shows up after `type` (Playing {message}, Watching {message})

Now is time to run the bot! Please see below.

### This script is to run managebot that updates itself at each restart/run. (RECOMMENDED)

```
sudo docker run -d \
--name=managebot \
--restart=unless-stopped \
--privileged \
-v /your/path/to/managebot:/your/path/to/managebot \
-v /var/run/docker.sock:/var/run/docker.sock \
-w /your/path/to/managebot \
python:3.11 \
/bin/bash -c "apt-get update -y && apt-get install git && apt-get install -y docker.io && python3 -m pip install -U py-cord --pre && git checkout -- bot.py && python3 bot.py"
```

### This script is to run managebot that DOES NOT update itself at each restart/run. (NOT RECOMMENDED)

```
sudo docker run -d \
--name=managebot \
--restart=unless-stopped \
--privileged \
-v /your/path/to/managebot:/your/path/to/managebot \
-v /var/run/docker.sock:/var/run/docker.sock \
-w /your/path/to/managebot \
python:3.11 \
/bin/bash -c "apt-get update -y && apt-get install -y docker.io && python3 -m pip install -U py-cord --pre && python3 bot.py"
```

### After choosing your run script, follow these instructions below.

Edit /your/path/to/managebot to wherever you put managebot.

**The first run of managebot usually takes around 2 minutes (depending on your internet speeds). This is just for the first run.**

Once your discord bot comes online. You are free to begin using commands.

## How to start, stop & restart the bot

The most simple way to start, stop or restart managebot is directly from the command line.

Start
```
sudo docker start managebot
```
Stop
```
sudo docker stop managebot
```
Restart
```
sudo docker restart managebot
```

# Issues

**Please report any issues you have with the bot in the Issues tab!**
