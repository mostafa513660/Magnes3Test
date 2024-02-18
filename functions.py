import asyncio

class get_info:
	def __init__(self, message):
		self.message = message
		self.type = ""
		self.is_group = False
		self.first_name = ""
		self.last_name = ""
		self.full_name = ""
		self.uid = 123
		self.cid = 123
		self.username = ""
		self.date = ""
		
	async def fetch_data(self):
		self.uid = self.message.from_user.id
		self.cid = self.message.chat.id
		self.type = self.message.chat.type
		self.date = self.message.date
		await self.fetch_username()
		await self.fetch_name()
		await self.chat_type()
		
	async def chat_type(self):
		type = self.type
		if type == "private":
			self.is_group = False
			return False
		else:
			self.is_group = True
			return True
	
	async def fetch_name(self):
		await self.chat_type()
		is_group = self.is_group
		if is_group:
			full_name = self.message.chat.title
		else:
			user = self.message.from_user
			first_name = user.first_name
			last_name = user.last_name if user.last_name is not None else ""
			self.first_name = first_name
			self.last_name = last_name
			full_name = first_name + last_name
		self.full_name = full_name
	
	async def fetch_username(self):
		await self.chat_type()
		is_group = self.is_group
		if is_group:
			username = self.message.chat.username
			if username is not None:
				username = "@" + username
			else:username = "Private Chat"
		else:
			username = self.message.from_user.username
			if username is not None:
				username = "@" + username
			else:username = "N/A"
		self.username = username

class some_fun:
	async def is_group(self, type):
		if type == "private":
			return False
		else:
			return True