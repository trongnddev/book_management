# from config.config_database import *
# from server.models.author import Author
# from server.models.book import *


# if __name__ == "__main__":
#     async def test():
#         new = Author(
#             author = 'Trong',
#             age = 1

#         )
#         await new.commit()

#     asyncio.run(test())

import asyncio
 

from config.config_redis import connection

async def set_key():
    val = await connection.execute('set', 'demo', 10)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(set_key())




from config.config_redis import conn

async def set_key():
    val = await conn.execute('set', 'demo', 10)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(set_key())


