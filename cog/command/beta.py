"""
BETA test commands
"""

# dependancies
import asyncio
import discord
from discord.ext import commands

# util
from utility.cog.player.player import Player

# characters
from utility.cog.character.list import c001_sabimen
from utility.cog.character.list import c002_sabimen
from utility.cog.character.list import c003_sabimen

class Cmd_beta(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.group()
    async def beta(self, ctx):
        return
    
    @beta.command()
    async def combat(self, ctx, user : discord.Member = None):
        """
        new combat system
        """
        # import
        from utility.cog.combat_system.combat import Combat
        from utility.cog.character.getter import Character_getter

        # init
        caller = Player(ctx, self.client, ctx.message.author)
        opponent = Player(ctx, self.client, user)
        getter = Character_getter()
        
        # set team
        opponent.team.team["a"] = await getter.get_character(4)
        opponent.team.team["b"] = await getter.get_character(2)
        opponent.team.team["c"] = await getter.get_character(1)

        opponent.name = "Test"

        if(opponent == None):
            opponent = caller

        teams = [
            {
                "owner" : caller,
                "team" : await caller.team.character()
            },
            {
                "owner" : opponent,
                "team" : await opponent.team.character()
            }
        ]

        combat = Combat(self.client, ctx, teams)

        await combat.run()

def setup(client):
    client.add_cog(Cmd_beta(client))