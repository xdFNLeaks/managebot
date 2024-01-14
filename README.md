# managebot

**Version 1.0.3 has been released!**

just a little project i'm working on that allows you to view and manage your docker containers from discord.

---

### What's New? *(v1.0.3)*

- Docker compose (hopefully works..)

---

### Features

- Executing Docker Commands (`/docker execute`) (start, stop, restart, pause, unpause, delete)
- Listing all docker containers and sorts them into Online & Offline. (`/list`)
- Docker Image Management + Image Pruning (`/docker images` | `/docker prune`)

### Planned Features

- Web Interface (possibly, not 100% sure if I can make this right now)

---

## Installation

Please create a `config` folder and inside a `config.json` file.

**Open `config.json` and edit it to your liking.**
- `token` = Your discord bot token. ([Discord Developer Portal](https://discord.com/developers/applications))
- `timezone_offset` = Your timezone offset. ([List of UTC offsets - Wikipedia](https://en.wikipedia.org/wiki/List_of_UTC_offsets))
- `guild_ids` = Your server ID. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `allowed_user_ids` = The ID of the bot admin. ([Tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
- `type` = The Rich Presence type (Playing ..., Watching ...) - Currently available: Playing, Watching, Listening.
- `message` = The message that shows up after `type` (Playing {message}, Watching {message})

Now is time to run the bot! Please see below.

### docker-compose.yaml (hopefully works lol)

```
version: "3.3"
services:
  managebot:
    container_name: managebot
    privileged: true
    restart: unless-stopped
    image: "ghcr.io/xdfnleaks/managebot:latest"
    volumes:
      - /your/path/to/managebot/config:/usr/src/app/config
      - /var/run/docker.sock:/var/run/docker.sock
```

Edit `/your/path/to/managebot` to wherever you put managebot.

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
