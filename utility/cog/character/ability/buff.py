"""
Represents a bonus effect

--

Author : DrLarck

Last update : 04/09/19 (DrLarck)
"""

# dependancies
import asyncio

# buff
class Buff:
    """
    Represents a bonus effect.

    - Parameter :

    `client` : Represents a `discord.Client` instance.

    `ctx` : Represents the `commands.Context`

    `team_a` | `b` : Represents the Ally team and the opponent team.

    - Attribute :

    `name` : default None - Represents the Buff's name.

    `description` : default None - Represents the Buff's description.

    `id` : default 0 - Represents the Buff's id.

    `icon` : default None - Represents the Buff's icon.

    `caster` : default None - Represents the Buff's caster.

    `initial_duration` : default 0 - Represents the Buff's initial duration.

    `duration` : default 0 - Represents the Buff's current duration.

    `max_stack` : default 0 - Represents the Buff's max stacks.

    `stack` : default 0 - Represents the Buff's current stacks.

    - Method :

    :coro:`translate()` : Allows you to translate the Buff's strings.

    :coro:`apply()` : Applies the Buff's effect.

    :coro:`on_remove()` : Does something on remove.
    """

    # attribute
    def __init__(self, client, ctx, team_a, team_b):
        # basic
        self.client = client
        self.ctx = ctx
        self.team_a = team_a
        self.team_b = team_b

        # info
        self.name = None
        self.description = None
        self.id = 0
        self.icon = "<:notfound:617735236473585694>"
        self.caster = None

        # duration
        self.initial_duration = 0
        self.duration = 0

        # stack
        self.max_stack = 0
        self.stack = 0
    
    # method
    async def translate(self):
        return

    async def apply(self):
        return
    
    async def on_remove(self):
        return