import asyncio

import aioredis


async def main():
    # Redis client bound to single connection (no auto reconnection).
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        await conn.set("key2", "179")
        val = await conn.get("key2")
    print(val)


async def redis_pool():
    # Redis client bound to pool of connections (auto-reconnecting).
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    await redis.set("key1", "110")
    val = await redis.get("key1")
    print(val)


async def demo1():
    redis =  aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    await redis.set('trong_key', 'NguyenDoTrong')
    bin_value = await redis.get('trong_key')
    
    # str_value = await redis.get('trong_key', encoding='utf-8')
    # assert str_value == 'trong_key'

   

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(redis_pool())
    asyncio.run(demo1())