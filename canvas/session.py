import aiohttp
import asyncio

async def init():
    async with aiohttp.ClientSession() as r:
        r.get("Hello")
