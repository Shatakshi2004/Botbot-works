import discord
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('meme'):
            await message.channel.send(get_meme())

        if message.content.startswith('hello'):
            await message.channel.send('Hello, I am Shatakshi!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("ERROR: DISCORD_TOKEN not found in .env file")
else:
    client.run(TOKEN)


