# managebot

just a little project i'm working on that allows you to view and manage your docker containers from discord.

---

### Features

- Executing Docker Commands (/docker execute) (currently only Start, Stop & Restarting docker containers.)
- Listing all docker containers and sorts them into Online & Offline. (/list)

### Planned Features

I currently do not have any plans. Check back in the future!

---

## Installation

**You must have docker installed and running.**

To run this, first clone this repository:

```
git clone https://github.com/xdFNLeaks/managebot.git
```

**After you have cloned this repo, open `config.json` and edit it to your liking.**
- `token` = Your discord bot token. ([Discord Developer Portal](https://discord.com/developers/applications))
- `timezone_offset` = Your timezone offset. ([List of UTC offsets - Wikipedia](https://en.wikipedia.org/wiki/List_of_UTC_offsets))
- `guild_ids` = Your server ID. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `allowed_user_ids` = The ID of the bot admin. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `type` = The Rich Presence type (Playing ..., Watching ...) - Currently available: Playing, Watching, Listening.
- `message` = The message that shows up after `type` (Playing {message}, Watching {message})

Once you have configured `config.json`, run the following command:

```
docker run -d \
--name=managebot \
--restart=unless-stopped \
--privileged \
-v /your/path/to/managebot:/your/path/to/managebot \
-v /var/run/docker.sock:/var/run/docker.sock \
-w /your/path/to/managebot \
python:3.11 \
/bin/bash -c "apt-get install -y docker.io && python3 -m pip install -U py-cord --pre && python3 bot.py"
```
Edit /your/path/to/managebot to wherever you put managebot.

**The first run of managebot usually takes around 2 minutes (depending on your internet speeds). This is just for the first run.**

Once your discord bot comes online. You are free to begin using commands.

## How to start, stop & restart the bot

The most simple way to start, stop or restart managebot is directly from the command line.

Start
```
docker start managebot
```
Stop
```
docker stop managebot
```
Restart
```
docker restart management
```
