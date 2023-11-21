import asyncio
import time


async def asset_function(delay):
    print("this is an asset function for other functions")
    if delay:
        time.sleep(delay)
        return delay
    return None


async def dependent_function():
    print("this function is dependent on another function")
    money = await asset_function(delay=None)
    if money:
        print("asset function provide money")
    else:
        print("money not provided by asset function")


asyncio.run(dependent_function())