import asyncio, aiomysql
from config import ACONVARS
from functions import some_fun

async def get_plan(cid, type):
	try:
		async with aiomysql.connect(**ACONVARS) as con:
			async with con.cursor() as cur:
				is_group = some_fun().is_group(type)
				if not is_group:
					await cur.execute("SELECT plan FROM users WHERE cid = %s", (cid,))
				else:
					await cur.execute("SELECT plan FROM groops WHERE cid = %s", (cid,))
				plan = await cur.fetchone()
				plan = plan[0] if plan else "Not Registed"
				return plan
	except: return "Not Registed"

class db_info:
	async def insert_new(self, cmd, values):
		try:
			pool = await aiomysql.create_pool(**ACONVARS)
			async with pool.acquire() as con:
				async with con.cursor() as cur:
					
					await cur.execute(cmd, values)
					await con.commit()
			pool.close()
			await pool.wait_closed()
		except Exception as e:print(e)
	
	async def check_exsits(self, table, cid):
		try:
			pool = await aiomysql.create_pool(**ACONVARS)
			async with pool.acquire() as con:
				async with con.cursor() as cur:
					await cur.execute("SELECT plan FROM {} WHERE cid = %s".format(table), (cid,))
					is_it = await cur.fetchone()
					is_it = is_it[0] if is_it else False
			pool.close()
			await pool.wait_closed()
			return is_it
		except Exception as e:
			print(e); return False