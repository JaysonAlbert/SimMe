import asyncio
from wechaty_puppet_itchat import PuppetItChat
from wechaty_puppet import PuppetOptions
from wechaty import Wechaty, WechatyOptions, Message


class Bot(Wechaty):
    async def on_message(self, msg: Message):
        print(msg)


async def main():
    options = WechatyOptions(
        puppet=PuppetItChat(PuppetOptions())
    )
    bot = Bot(options)
    await bot.start()

asyncio.run(main())

