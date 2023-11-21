# print("Yashdeep Singh")
#
# print("Python Developer")


import asyncio
import time


async def execute(delay, value):
    await asyncio.sleep(delay)
    print(value)
    return value


async def main():
    print(f"started at {time.strftime('%X')}")

    data1 = await execute(1, 'hello')
    if data1:
        await execute(20, 'first function executed after 20 seconds')
    else:
        print("something went wrong")

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())