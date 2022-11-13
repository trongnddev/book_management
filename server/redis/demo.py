import asyncio

from config.config_redis import conn

async def set_key():
    val = await conn.execute('set', 'demo', 10)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(set_key())


