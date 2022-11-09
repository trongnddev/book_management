from config.config_database import *
from server.models.author import Author
from server.models.book import *


if __name__ == "__main__":
    async def test():
        new = Author(
            author = 'Trong',
            age = 1

        )
        await new.commit()

    asyncio.run(test())
