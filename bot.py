import json, discord, datetime
from discord.ext import commands
from discord.ui import Button
from discord import app_commands, Embed, Interaction
from typing import Optional, List
from quran import chapters

def join_words(words):
    max_length = 4096
    delimiter = "\n"
    result = ""
    current_length = 0

    for word in words:
        word_length = len(word) + len(delimiter)
        
        # Check if adding the current word exceeds the length limit
        if current_length + word_length > max_length:
            break
        
        result += word + delimiter
        current_length += word_length

    # Remove the trailing delimiter
    result = result.rstrip(delimiter)

    return result


with open('config.json', 'r') as f:
  config = json.load(f)

class QurAnClient(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.all(), owner_id=1110526906106904626)
    self.synced = False
  
  async def on_ready(self):
    if not self.synced:
      await tree.sync()
      self.synced = True
      
      print(f"Synced {len(tree.get_commands())} commands")

  async def on_guild_join(self, guild):
    permissions = guild.me.guild_permissions
    if not permissions.use_application_commands():
      owner = guild.owner()
      try:
        await owner.send(f"I do not have permissions to use application commands in **{guild.name}**. Please grant me application command permissions so users can use my commands")
      except discord.Forbidden:
        try:
          await self.send_friend_request(owner)
        except discord.Forbidden:
          with open("owner.txt", "w") as f:
            f.write(f"{owner}\n")
            f.close()

  async def on_friend_request(self, request):
        if request.user.id == self.owner_id:
            await request.accept()
            await request.user.send("I do not have permissions to use application commands in one of your servers. Please check our mutual servers and grant me permissions to use application commands so members can use my commands")

client = QurAnClient()
tree = app_commands.CommandTree(client)

@tree.command()
@tree.app_commands.description("Extract all verses revealed in Madinah (complex or simple notation)")
@tree.app_commands.describe(simplified="Example: Al-Fatihah", complex="Example: Al-Fātiĥah", order="Do you want them in the order they were revealed?")
async def madinah(interaction: Interaction, simplified: Optional[bool]=None, complex: Optional[bool]=None, order: Optional[bool]=None):
    if simplified and complex and order is None:
        chp = chapters.Chapters()

        embed = Embed(title="All Verses Revealed in Madinah - Ordered", description=join_words(chp.all_complex_order()))
        embed.set_footer(text="/madinah", icon_url=client.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()

        await interaction.response.send_message(embed=embed, interaction.user.mention)

client.run(config["TOKEN"])