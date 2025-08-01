import discord
import requests
import json
import random

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        response.raise_for_status()
        json_data = response.json()
        return json_data['url']
    except Exception as e:
        print(f"Error fetching meme: {e}")
        return "Sorry, I couldn't fetch a meme."

# making random message choices
phrases = ["fuck you", "sigma", "jakob likes boys", "sharkpark", "skrrrrrrrrrrt", "uh idk im drinking a dr pepper rn and ran out of ideas for phrases", "look mom i made a bot!!!", "python lowk kinda chill"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        
        if message.content.startswith('$test'):
            await message.channel.send(random.choice(phrases))

        if message.content.startswith('$ig'):
            await message.channel.send('https://www.instagram.com/concaveshark?igsh=MXJ4NXlxMHphbXRybQ==')

        if message.content.startswith('$playlist'):
            await message.channel.send('https://open.spotify.com/playlist/0PcqRwOgwXrjJ37jHJahZi?si=53383ca0c0e84393')

        if message.content.startswith('how to league'):
            await message.channel.send('https://cdn.discordapp.com/attachments/1086036245660061829/1233853943977607340/attachment.gif?ex=688db648&is=688c64c8&hm=a095dcc76bc2cabfbbc9d1254afc0c60b9d22c152794d926f1a3600d1cfc60dc&')

        if message.content.startswith('ducktwerk'):
            await message.channel.send('<a:duck_twerk:1400791761583997049>')
            await message.add_reaction("<a:duck_twerk:1400791761583997049>")

        if message.content.startswith('$help'):
            await message.channel.send('commands:\n$meme: sends a generated meme\n$test: sends a response\n$ig: sends my instagram\n$playlist: sends my playlist\nhow to league\nducktwerk')

# setting intents for the discord bot to use
intents = discord.Intents.default()
intents.message_content = True # this means it can only send messages

client = MyClient(intents=intents)
client.run('token here')

