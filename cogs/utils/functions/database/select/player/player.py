'''
Manages the function which select the player's informations from player table.

Last update: 08/05/19
'''

# Dependancies

import asyncpg, time

async def Select_player_name(client, player):
    '''
    Returns the player name or `None` if not found.

    `client` : must be `discord.Client` object or `discord.ext.commands.AutoShardedBot` one.

    `player` : must be `discord.Member` object.

    Return: str or None
    '''

    # Init

    conn = await client.db.acquire()

    query = 'SELECT player_name FROM player WHERE player_id = $1;'
    player_name = None

    try:
        player_name = await conn.fetchval(query, player.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.select.player.player.Select_player_name() : l.30 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(player_name)

async def Select_player_language(client, player):
    '''
    Return the player language as an `str` object.

    `client` : must be `discord.Client` or `discord.ext.commands.AutoShardedBot` object.

    `player` : must be `discord.Member` object.

    Return: str
    '''

    # Init

    conn = await client.db.acquire()

    query = 'SELECT language FROM player WHERE player_id = $1;'
    player_language = None

    try:
        player_language = await conn.fetchval(query, player.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} Error in cogs.utils.functions.database.select.player.player.Select_player_language() : l.61 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(player_language)