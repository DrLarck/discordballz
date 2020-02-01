"""
Mission command

--

Author : DrLarck

Last update : 01/02/20 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# checker
from utility.command.checker.basic import Basic_checker

# mission command
class Cmd_mission(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.command()
    async def mission(self, ctx, choice = None):
        """
        Allow the player to display the mission panel

        Or to start a mission if the `choice` parameter is != `None`

        - Parameter :

        `choice` (`int`) : Mission index
        """
    

def setup(client):
    client.add_cog(Cmd_mission(client))