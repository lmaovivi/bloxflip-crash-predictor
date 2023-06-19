import cloudscraper
import json
import discord
from discord import app_commands
cs = cloudscraper.create_scraper()
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

BOT_TOKEN = "MTExNDUyNzk3MjQ5ODYwNDA0Mw.GreJQb.58CV4-AeHK4tfA14A05ryk18-f_TOpM0oazVxw"
PREDICTOR_NAME = 'idk'
client = aclient()
tree = app_commands.CommandTree(client)



@tree.command(name='crash', description='Crash prediction made simple, made by evi#4204')
async def crash(interaction: discord.Interaction):
    data = cs.get("https://api.bloxflip.com/games/crash").json() # uses bloxflip api to get the response in json, if predictions dont work replace the link with this https://rest-bf.blox.land/games/crash
    cp1 = data['history'][0]['crashPoint'] # look in history for last crash point
    cp2 = data['history'][1]['crashPoint']
    cp3 = data['history'][2]['crashPoint']
    cp4 = data['history'][3]['crashPoint']
    prediction = cp1 / cp2 # divides cp1 and cp2 to get prediction
    if prediction < 1.01:
        embed = discord.Embed(color=0xffd700)
        embed.add_field(name="**Error!**", value="Failed to predict, try next game!")
        embed.set_footer(text=f"Brought to you by {PREDICTOR_NAME}, credit to evi#4204") # please keep credits and if you don't i will take down your server.
        await interaction.response.send_message(embed=embed)
    else:
     embed = discord.Embed(color=0xffd700)
     embed.add_field(name="Prediction:", value=f"{prediction:.2f}")
     embed.add_field(name='Last Games:', value=f"{cp1}x, {cp2}x,{cp3}x, {cp4}x") # i think its pretty understandable 🤓🤓
     embed.set_footer(text=f"Brought to you by {PREDICTOR_NAME}, credit to evi#4204") # please keep credits and if you don't i will take down your server.
     await interaction.response.send_message(embed=embed)


client.run(BOT_TOKEN)
