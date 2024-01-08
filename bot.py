import discord
import subprocess
import socket
import platform
from datetime import datetime, timedelta, timezone
import json

bot = discord.Bot()

with open("config.json", "r") as config_file:
    config = json.load(config_file)

def get_current_time():
    local_timezone = timezone(timedelta(hours=config["timezone_offset"]))
    current_time = datetime.now(local_timezone).strftime("%I:%M %p - %d/%m/%Y")
    return current_time

async def get_container_names(ctx: discord.AutocompleteContext):
    try:
        result = subprocess.check_output(['docker', 'ps', '--all', '--format', '{{.Names}}'], text=True)
        container_names = result.split('\n')
        container_names = [name for name in container_names if name]
        return container_names

    except subprocess.CalledProcessError as e:
        return []

@bot.event
async def on_ready():
    activity_type = config["status"]["type"]
    activity_message = config["status"]["message"]

    if activity_type == "playing":
        activity = discord.Game(name=activity_message)
    elif activity_type == "listening":
        activity = discord.Activity(type=discord.ActivityType.listening, name=activity_message)
    elif activity_type == "watching":
        activity = discord.Activity(type=discord.ActivityType.watching, name=activity_message)
    else:
        activity = None

    await bot.change_presence(activity=activity)
    print("Bot online!")

docker_management = bot.create_group("docker", "Manage Docker containers")

@docker_management.command(description="Execute Docker container management commands.")
async def execute(ctx, action: discord.Option(str, choices=['start', 'stop', 'restart']), container_name: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_container_names))):
    if ctx.author.id not in config["allowed_user_ids"]:
        await ctx.respond("You are not authorized to use this bot.")
        return

    try:
        response = ""
        if action.lower() == "start":
            subprocess.check_output(['docker', 'start', container_name])
            response = f"Container `{container_name}` has been started."
        elif action.lower() == "stop":
            subprocess.check_output(['docker', 'stop', container_name])
            response = f"Container `{container_name}` has been stopped."
        elif action.lower() == "restart":
            subprocess.check_output(['docker', 'restart', container_name])
            response = f"Container `{container_name}` has been restarted."
        else:
            await ctx.respond("Invalid action. Use 'start', 'stop', or 'restart'.")

        embed = discord.Embed(
            title="**__Docker Management__**",
            description=response,
            color=discord.Colour.blurple(),
        )
        embed.set_footer(text=get_current_time())
        await ctx.respond(embed=embed)

    except subprocess.CalledProcessError as e:
        await ctx.respond(f"Error executing Docker command: {e}")

@bot.slash_command(guild_ids=config["guild_ids"], description="List All Docker Containers")
async def list(ctx):
    if ctx.author.id not in config["allowed_user_ids"]:
        await ctx.respond("You are not authorized to use this bot.")
        return

    try:
        result = subprocess.check_output(['docker', 'ps', '--all', '--format', '{{.Names}}\t{{.Status}}'], text=True)

        containers_info = result.split('\n')
        containers_info = [line.split('\t') for line in containers_info if line]

        online_containers = [f"**{container_name}**: `{container_status}`" for container_name, container_status in containers_info if "Up" in container_status]
        offline_containers = [f"**{container_name}**: `{container_status}`" for container_name, container_status in containers_info if "Up" not in container_status]

        embed = discord.Embed(
            title="**__Docker Container(s) Status__**",
            color=discord.Colour.blurple(),
        )

        if online_containers:
            embed.add_field(name=":green_circle: **__Online__**", value="\n".join(online_containers), inline=False)

        if offline_containers:
            embed.add_field(name=":red_circle: **__Offline__**", value="\n".join(offline_containers), inline=False)

        embed.set_footer(text=get_current_time())
        await ctx.respond(embed=embed)

    except subprocess.CalledProcessError as e:
        await ctx.respond(f"Error retrieving Docker instances: {e}")

bot.run(config["token"])
