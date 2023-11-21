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
<<<<<<< HEAD:app_file/asyncio_test.py
    money = await asset_function(delay=None)  # change delay time accordingly
=======
    money = await asset_function(delay=None)
>>>>>>> 40d0abb2d824fb7f2d2a8d5ef30b09a538405b6f:app_file/asyncio_test.py
    if money:
        print("asset function provide money")
    else:
        print("money not provided by asset function")


asyncio.run(dependent_function())

print("asuncio-feature branch re-activation")