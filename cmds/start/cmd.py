from bot_connection import bot
from databaseFuns import get_plan, db_info
from functions import  get_info

@bot.message_handler(commands=['start'])
async def start_message(message):
	chat_id = message.chat.id
	type = message.chat.type
	g = get_info(message)
	await g.fetch_data()

	await bot.reply_to(message,f"Your plan:  {g.full_name}, {g.cid,g.uid}, {g.type}, {g.is_group}, {g.username}, {g.chat_type}")
	test = db_info()
	joined = await test.check_exsits("users", g.cid)
	if joined:
		await bot.reply_to(message,"You are joined to the bot")
