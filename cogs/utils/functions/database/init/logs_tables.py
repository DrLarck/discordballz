'''
Manages the creation of the logs tables.

Last update: 27/05/19
'''

# Dependancies

import asyncpg, time

async def Create_logs_tables(client):
    '''
    Create the logs tables.

    Return: void
    '''

    # Init

    conn = await client.db.acquire()  # Open the connection to the database, `conn`

    # Logs : commands

    query = '''
    CREATE TABLE IF NOT EXISTS logs_commands(
        day TEXT,
        hour TEXT,
        command_name TEXT,
        caller_name TEXT,
        caller_id BIGINT,
        target_name TEXT DEFAULT 'NONE',
        target_id BIGINT DEFAULT '0'
    );'''

    try:
        await conn.execute(query)
        query = ''
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in cogs.utils.functions.database.init.Create_logs_table() : l.33 - 35 : {}'.format(error_time, error))
        pass
    
    # End

    await client.db.release(conn)