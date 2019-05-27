'''
Manages the character tables creation.

Last update: 27/05/19
'''

# Dependancies

import asyncpg, time
from time import strftime, gmtime

async def Create_unique_character_table(client):
    '''
    Create the unique character table.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''
    CREATE SEQUENCE IF NOT EXISTS unique_characters_reference_seq;
    CREATE TABLE IF NOT EXISTS unique_characters(
        reference BIGINT PRIMARY KEY DEFAULT nextval('unique_characters_reference_seq') NOT NULL,
        unique_id TEXT DEFAULT 'NONE',
        global_id BIGINT,
        player_id BIGINT
        );'''
    
    query_contraint = 'CREATE UNIQUE INDEX IF NOT EXISTS reference ON unique_characters(reference);'

    try:
        await conn.execute(query)
        await conn.execute(query_contraint)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.init.character_tables.Create_unique_character_table() : l.35 - 36 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Create_characters_table(client):
    '''
    Creates the tables that will contains all the characters informations.

    `client` : must be `discord.Client` object.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()

    query = '''
    CREATE SEQUENCE IF NOT EXISTS characters_reference_seq;
    CREATE TABLE IF NOT EXISTS characters(
        reference BIGINT PRIMARY KEY DEFAULT nextval('characters_reference_seq') NOT NULL,
        global_id BIGINT DEFAULT 0,
        name TEXT DEFAULT 'NONE',
        image_url TEXT DEFAULT 'NONE',
        base_rarity TEXT DEFAULT 'NONE',
        type TEXT DEFAULT 'NONE',
        base_hp BIGINT DEFAULT 1,
        base_min_dmg BIGINT DEFAULT 0,
        base_max_dmg BIGINT DEFAULT 1
    );'''

    query_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS global_id ON characters(global_id, reference);'

    try:
        await conn.execute(query)
        await conn.execute(query_constraint)
    
    except Exception as error:
        error_time = strftime('%d/%m/%y - %H:%M', gmtime())
        print('{} Error in cogs.utils.functions.database.init.character_tables.Create_characters_table() : l.71 - 72 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)