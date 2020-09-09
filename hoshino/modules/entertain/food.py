import hoshino
from hoshino import Service
from datetime import datetime
import os
from os import path
from nonebot import MessageSegment
import random

sv = Service('好看的东西', bundle='pcr娱乐', help_='''
来点好看的   |  一些好~看~的~图~片
'''.strip())

START = 22
END = 3

res_path = path.abspath(path.join(path.expanduser(hoshino.config.RES_DIR),'food'))
if not path.exists(res_path):
	os.makedirs(res_path)

res_dir = os.listdir(res_path)
random.shuffle(res_dir)
res_idx = 0

@sv.on_fullmatch(('来点好看的','来点好康的'))
async def send_food_pic(bot,event):
	global res_dir,res_idx

	now = datetime.now()
	if END<=now.hour<START:
		await bot.send(event,f'这个功能只在{START}点到{END}点开放哟', at_sender=True)
		return

	if len(res_dir)==0:
		await bot.send(event,'没什么好看的，快去睡觉！',at_sender=True)
		return

	pic = res_dir[res_idx]
	res_idx = (res_idx+1) % len(res_dir)
	pic_path = path.join(res_path,pic)
	await bot.send(event,MessageSegment.image(f'file:///{pic_path}'))

@sv.on_fullmatch(('刷新好看的','刷新好康的'))
async def renew_food_pic(bot,event):
	global res_dir,res_idx

	res_dir = os.listdir(res_path)
	random.shuffle(res_dir)
	res_idx = 0

	await bot.send(event,f'刷新成功，现在有{len(res_dir)}张好看的~')