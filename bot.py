import json, discord
from discord.ext import commands
from discord.ui import Button
from discord import app_commands, Embed, Interaction
from typing import Optional, List

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

client.run(config["TOKEN"])