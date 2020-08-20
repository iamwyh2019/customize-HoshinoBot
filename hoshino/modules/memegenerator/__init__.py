from io import BytesIO
from hoshino import Service
from nonebot import MessageSegment
import os
from os import path
from .memeutil import draw_meme
from PIL import Image
import base64

img_dir = path.join(path.abspath(path.dirname(__file__)),"meme/")
img = []
img_name = []

def load_images():
	global img,img_name,img_dir
	img = os.listdir(img_dir)
	img.sort()
	img_name = [''.join(s.split('.')[:-1]) for s in img]

load_images()

sv_help = '''
[表情列表] 查看当前表情列表
[查看表情 <名字>] 查看指定表情
[生成表情 <名字> <文案>] 生成一张表情
'''.strip()

sv = Service('表情生成器', help_=sv_help, bundle='表情生成器')

@sv.on_fullmatch(('表情列表','查看表情列表'))
async def show_memes(bot,event):
	msg = "当前表情有："
	for meme in img_name:
		msg += "\n" + meme
	await bot.send(event,msg,at_sender=True)

@sv.on_fullmatch(('更新表情','刷新表情','更新表情列表','刷新表情列表'))
async def reload_memes(bot,event):
	load_images()
	await bot.send(event,f"表情列表更新成功，现在有{len(img)}张表情")

@sv.on_prefix(('查看表情','看看表情'))
async def show_meme(bot,event):
	msg = event.message.extract_plain_text().split(" ")
	sel = msg[0]
	if sel not in img_name:
		await bot.send(event,f'没有找到表情"{sel}"',at_sender=True)
		return

	idx = img_name.index(sel)
	await bot.send(event,
		MessageSegment.image(f'file:///{os.path.join(img_dir,img[idx])}'))

@sv.on_prefix(('生成表情',))
async def generate_meme(bot,event):
	msg = event.message.extract_plain_text().split(" ")
	sel = msg[0]
	if sel not in img_name:
		await bot.send(event,f'没有找到表情"{sel}"',at_sender=True)
		return

	idx = img_name.index(sel)
	image = Image.open(os.path.join(img_dir,img[idx]))
	message = " ".join(msg[1:])
	message = message.replace("\r","\n")
	meme = draw_meme(image,message)

	buf = BytesIO()
	meme.save(buf,format='JPEG')
	base64_str = f'base64://{base64.b64encode(buf.getvalue()).decode()}'
	await bot.send(event, f'[CQ:image,file={base64_str}]')
