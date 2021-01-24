import discord  
import os

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is logged in as {0.user}".format(client))


@client.event
async def on_message(message_trigger):
    if message_trigger.author == client.user:
        return  
    if message_trigger.content.startswith("hi"):
        await message_trigger.channel.send("Hello")

    if message_trigger.content.startswith("I am returning your nose. I found it in my business."):
        await message_trigger.channel.send("Shutup, okay. Your insults are pathetic @evilbot.")

client.run(os.getenv("TOKEN"))

















