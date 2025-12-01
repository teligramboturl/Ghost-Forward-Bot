# Don't Remove Credit Tg - @Tech_Shreyansh1
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TechShreyansh
# Ask Doubt on telegram @AboutsShreyansh

import asyncio, logging
from config import Config
from pyrogram import Client as Ghost, idle
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# Don't Remove Credit Tg - @Tech_Shreyansh1
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TechShreyansh
# Ask Doubt on telegram @AboutsShreyansh

if __name__ == "__main__":
    GhostBot = Ghost(
        "Ghost-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins")
    )  
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
               
    async def main():
        await GhostBot.start()
        bot_info  = await GhostBot.get_me()
        await restart_forwards(GhostBot)
        print("Bot Started.")
        await idle()

    asyncio.get_event_loop().run_until_complete(main())

# Don't Remove Credit Tg - @Tech_Shreyansh1
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TechShreyansh
# Ask Doubt on telegram @AboutsShreyansh
