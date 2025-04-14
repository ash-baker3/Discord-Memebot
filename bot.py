import discord
import requests
import json
import random
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')

def get_meme():
    response = requests.get('https://api.imgflip.com/get_memes')
    json_data = json.loads(response.text)

    memes = json_data['data']['memes']
    meme = random.choice(memes)

    return meme['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('#meme'):
            await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(api_key)

