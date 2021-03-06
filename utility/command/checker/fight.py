"""
Regroups the fight checker

--

Author : DrLarck

Last update : 16/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter

# fight checker
class Fight_checker:
    """
    Represents the fight checker
    """

    in_fight = []

    # method
    async def is_in_fight(self, ctx):
        """
        `coroutine`

        Check if the player is in fight or not.

        --

        Return : Bool
        """

        # init
        can_fight = True
        player = ctx.message.author

        if player.id in self.in_fight:
            can_fight = False
            
            await ctx.send(f"<@{player.id}> ❌ You are already in a fight.")

        return(can_fight)
    
    async def is_fighting(self, ctx):
        """
        `coroutine`

        This function checks if the player is still fighting or not.

        This one is used to check if the continue has to be stoped if the player has quit using the `cancel fight` command.

        --

        Return : bool
        """

        # init
        player = ctx.message.author

        if player.id in self.in_fight:
            return(True)
        
        return(False)

    async def has_team(self, ctx):
        """
        `coroutine`

        Check if the player has set a team or not

        --

        Return : bool
        """

        # init
        player = Player(ctx, ctx.bot, ctx.message.author)
        getter = Character_getter()
        player_team = await player.team.get_team()
        has_fighter = False

        # check if the player has setted up fighters
        if(type(player_team["a"]) == str):
            fighter = await getter.get_from_unique(ctx.bot, player_team["a"])  # check if the fighter exists
            if(fighter != None):
                has_fighter = True
        
        if(type(player_team["b"]) == str):
            fighter = await getter.get_from_unique(ctx.bot, player_team["b"])
            if(fighter != None):
                has_fighter = True
            
        if(type(player_team["c"]) == str):
            fighter = await getter.get_from_unique(ctx.bot, player_team["c"])
            if(fighter != None):
                has_fighter = True

        if not has_fighter:
            await ctx.send(f"<@{player.id}> You did not **set any fighter**, in consequence to it, you cannot use this command.\nUse `d!team` for more informations.")

        return(has_fighter)