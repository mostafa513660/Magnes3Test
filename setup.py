import mysql.connector as sql
from config import (CONVARS)

con = sql.connect(**CONVARS)

cur = con.cursor()
#—–—–————SETTINGS—————–—–—#
cur.execute("DROP TABLE IF EXISTS settings")

cur.execute("""
CREATE TABLE IF NOT EXISTS settings(
	botWorking BOOLEAN,
	checkWorking BOOLEAN,
	scrapWorking BOOLEAN)
""")

cur.execute("INSERT INTO settings VALUES(1, 1, 1)")
#—–—–—————USERS——————–—–—#
cur.execute("DROP TABLE IF EXISTS users")

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
 id INT AUTO_INCREMENT PRIMARY KEY,
 uid BIGINT,
 cid BIGINT,
 account_data TEXT,
 join_date TEXT,
 anti_spam VARCHAR(255) DEFAULT 'No',
 plan VARCHAR(255) DEFAULT 'Free',
 planExDate VARCHAR(255) DEFAULT 'Forever')
""")
#—–—–—–———GROUPS—————–—–—#
cur.execute("DROP TABLE IF EXISTS groops")

cur.execute("""
CREATE TABLE IF NOT EXISTS groops(
 id INT AUTO_INCREMENT PRIMARY KEY,
 cid BIGINT,
 group_data TEXT,
 join_date TEXT,
 anti_spam VARCHAR(255) DEFAULT 'No',
 plan VARCHAR(255) DEFAULT 'Free',
 planExDate VARCHAR(255) DEFAULT 'Forever')
""")
#—–—–—————PLANS——————–—–—#
cur.execute("DROP TABLE IF EXISTS plans")

cur.execute("""
CREATE TABLE IF NOT EXISTS plans(
	name TEXT,
	canCheck BOOLEAN,
	canScrap BOOLEAN,
	canEdit BOOLEAN,
	canUseAllGates BOOLEAN,
	useablsGates TEXT,
	useableTools TEXT,
	antiSpamTime INTEGER)
""")

cur.execute(
"""INSERT INTO plans
VALUES ("Owrner",1,1,1,1,"All","All",0)""")
cur.execute(
"""INSERT INTO plans
VALUES ("Admin",1,1,1,1,"All","All",0)""")
cur.execute(
"""INSERT INTO plans
VALUES ("Premium",1,1,0,1,"All","All",10)""")
cur.execute(
"""INSERT INTO plans
VALUES ("Free",0,0,0,0,NULL,NULL,30)""")
#—–—–—————GATES——————–—–—#
cur.execute("DROP TABLE IF EXISTS gates")

cur.execute("""
CREATE TABLE IF NOT EXISTS gates(
	name TEXT,
	type TEXT,
	command TEXT,
	lastUpdate TEXT,
	status BOOLEAN)
""")
#—–—–———SCRAP-CARDS———–—–—#
cur.execute("DROP TABLE IF EXISTS scrcards")

cur.execute("""
CREATE TABLE IF NOT EXISTS scrcards(
	card TEXT)
""")

#—–—–———————————————–—–—#
con.commit()