from bot_connection import bot
import json, time, asyncio, aiomysql, traceback
from databaseFuns import db_info
from functions import  get_info
from config import ACONVARS

@bot.message_handler(commands=['register'])
async def start_message(message):
#—–—–———————————————–—–—#
	start_time = time.time()
	db = db_info()
#—–—–———————————————–—–—#
	info = get_info(message)
	await info.fetch_data()
	uid = info.uid ; cid = info.cid
	type = info.type ; date = info.date
	name = info.full_name
	username = info.username
	is_group = info.is_group
	data = {
		"uid": uid if uid == cid else cid,
		"name": name,
		"username": username,
		"is_group": is_group,
		"chat_type": type
		}
	acc_data = json.dumps(data, ensure_ascii=False).encode('utf8').decode()
#—–—–———————————————–—–—#
	#joined = await is_joined(cid, type)
	
	
	if await db.check_exsits("users",cid):
		await bot.send_message(cid,"You Are Already Registered In The BoT")
		return
	await signup(uid, acc_data, date, cid, is_group)

	end = time.time()
	formatted_time = "{:.2f}".format(end - start_time)

	if is_group:
		await bot.send_message(cid, f"Successful Group Registration\n Group Name: [{name}](tg://user?id={cid})\n Group Username: `{username}`\n Group ID: `{cid}`\nin Time: {formatted_time}",parse_mode="Markdown");return 
	else:
		await bot.send_message(cid, f"Successful Registration\n Your Name: [{name}](tg://user?id={uid})\n Your Username: `{username}`\n Your ID: `{uid}`\nin Time: {formatted_time}",parse_mode="Markdown");return
#—–—–———————————————–—–—#
#async def signup(uid, acc_data, date, cid, is_group):
#	try:
#		pool = await aiomysql.create_pool(**ACONVARS)
#		async with pool.acquire() as con:
#			async with con.cursor() as cur:
#				if not is_group:
#					await cur.execute(
#"""INSERT INTO 
#users(uid, cid, account_data, join_date)
#VALUES (%s, %s, %s, %s)""",
#					(uid, cid, acc_data, date))
#				else:
#					await cur.execute(
#"""INSERT INTO 
#groops(cid, group_data, join_date)
#VALUES (%s, %s, %s)""",
#					(cid, acc_data, date))
#				await con.commit()
#				return pool.close()
#	except Exception as e:
#		print(e)
#		traceback.print_exc()
#		return

async def signup(uid, acc_data, date, cid, is_group):
	try:
		db = db_info()
		if not is_group:
			cmd = (
"""INSERT INTO 
users(uid, cid, account_data, join_date)
VALUES (%s, %s, %s, %s)""")
			
			values = (uid, cid, acc_data, date)
			await db.insert_new(cmd, values)
		else:
			cmd = (
    """INSERT INTO 
    groops(cid, group_data, join_date)
    VALUES (%s, %s, %s)"""
)
			values = (cid, acc_data, date)
			await db.insert_new(cmd, values)
	except Exception as e:
		print(e)
		traceback.print_exc()
		return