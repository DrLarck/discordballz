"""
Damage object

--

Author : DrLarck

Last update : 19/02/20 (DrLarck)
"""

# dependancies
import asyncio

# graphic
from configuration.icon import game_icon

class Damage():
    """
    Represents the damage dealt by an ability

    - Parameter 

    `physical` (`int`) 

    `ki` (`int`)

    `true` (`int`)

    """

    def __init__(self, physical = 0, ki = 0, true = 0):
        self.physical = physical
        self.ki = ki
        self.true = true
    
    async def get_display(self):
        """
        `coroutine`

        Generate the damage display

        --

        Return : `str`
        """

        # init
        total_damage = self.physical + self.ki + self.true
        display = f"__Damage__ : - **{total_damage:,}**"
        detail_cpt = 0

        # display the detailed damages
        if(total_damage > 0):
            # add parenthesis to display the detailed damage
            display += " ("

            # add the physical details
            if(self.physical > 0):
                display += f"*-{self.physical:,}*:punch:"
                detail_cpt += 1

            # add the ki detail
            if(self.ki > 0):
                if(detail_cpt > 0):
                    # add a separator if there is already a detail before it
                    display += " | "
                
                display += f"*-{self.ki:,}*{game_icon['ki_ability']}"
                detail_cpt += 1
            
            # add true detail
            if(self.true > 0):
                if(detail_cpt > 0):
                    display += " | "
                
                display += f"*-{self.true:,}*:anger:"

            # close the parenthesis
            display += ")"

        return(display)