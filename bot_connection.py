import asyncio
from config import TOKEN

from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot(TOKEN)

from register.command import *
from cmds.start.cmd import *

if __name__ == "__main__":
	asyncio.run(bot.polling(non_stop=True))
#—–—–———————————————–—–—#
#bot.send_message(5314185723,"started")
import time 
time.sleep(3)
from setup import *
