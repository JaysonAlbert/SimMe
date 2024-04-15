import asyncio
from wechaty_puppet_itchat import PuppetItChat
from wechaty_puppet import PuppetOptions
from wechaty import Friendship, Wechaty, WechatyOptions, Message, FriendshipType
import re
from loguru import logger

# Configure logger to write to a file
# Here, the log file rotates when it reaches 5 MB
logger.add("logs/bot.log", rotation="5 MB")

class Bot(Wechaty):

    friendship_verify = re.compile(r"票星球|咸鱼")

    async def on_message(self, msg: Message):
        logger.info(msg)
        
    async def on_friendship(self, friendship: Friendship) -> None:
        if friendship.type() == FriendshipType.Receive:
            match = self.friendship_verify.search(friendship.hello())
            if match:
                await friendship.accept()
                logger.info(f'Friendship received: {friendship.contact().name()}')
        elif friendship.type() == FriendshipType.Confirm:
            logger.info(f'Friendship confirmed: {friendship.contact().name()}')


async def main():
    options = WechatyOptions(
        puppet=PuppetItChat(PuppetOptions())
    )
    bot = Bot(options)
    await bot.start()

asyncio.run(main())

