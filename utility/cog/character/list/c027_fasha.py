"""
Represents Fasha

--

Author : Zyorhist

Last update : 06/02/20 (DrLarck)
"""

# dependancies
import asyncio

# util
from utility.cog.character.character import Character

class Character_027(Character):
    """
    Represents the Fasha unit from the Bardock saga.
    """

    def __init__(self):
        Character.__init__(self)

        # info
        self.info.name = "Fasha"
        self.info.id = 27
        self.info.saga = "Bardock"

        # stat
        self.health.maximum = 2375
        
        self.damage.physical_max = 625
        self.damage.ki_max = 775

        self.defense.armor = 475
        self.defense.spirit = 400
        self.defense.dodge = 15

        self.critical_chance = 30
       
        self.regeneration.ki = 2