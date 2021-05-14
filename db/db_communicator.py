import asyncpg
import asyncio
from services.common.config import DB_Config


async def db_connect():
    """
    Connects to the database and stores the connection in ``conn``.
    """
    try:
        conn = await asyncpg.connect(host=DB_Config.dbhost,
                                     port=DB_Config.dbport,
                                     database=DB_Config.dbname,
                                     user=DB_Config.dbuser,
                                     password=DB_Config.dbpass)
        return conn

    except (OSError, asyncio.TimeoutError, ConnectionError) as exc:
        # self.logger.error(exc)
        pass


CREATE_TABLE_STRUCTURE = '''
           CREATE TABLE IF NOT EXISTS status(
               id serial PRIMARY KEY,
               status_code text,
               url text,
               regex boolean
           )
       '''

sql_insert_table_statement = '''
                   INSERT INTO status(id, status_code, url, regex) VALUES($1, $2, $3, $4)
               '''


async def database_writing(data):
    connection = await db_connect()
    await connection.execute(CREATE_TABLE_STRUCTURE)
    await connection.execute(sql_insert_table_statement,
                             3,
                             str(data['status_code']),
                             data['url'],
                             data['regex_matching'], )

    await connection.close()
