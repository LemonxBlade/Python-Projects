import discord
import random

#  SECRET FILE  #
API_TOKEN = "Token key plz"
client = discord.Client()
#  SECRET FILE  #

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Get username, message, and channel
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # ❌ Make sure bot doesn't respond to itself
    if message.author == client.user:
        return

    # 🗣 Responds to messages in 'general'
    if channel == 'memes':
        if user_message == 'yo':
            response = f'Hello {username}'
            await message.channel.send(response)
            return
        elif user_message == 'bye':
            response = f'Have a nice day, {username}!'
            await message.channel.send(response)
            return
        elif user_message == 'OwO':
            response = f'OwO! {username}!'
            await message.channel.send(response)
            return

    # giveaway
    if channel == 'private-bot-channel':
        if user_message == '!random':
            random_number = random.randrange(1000)
            response = f'Random number: {random_number}'
            await message.channel.send(response)
            return

client.run(API_TOKEN)