# TODO: rewrite this


import random
from datetime import timedelta

import nonebot
from nonebot import Message, MessageSegment, message_preprocessor, on_command
from nonebot.message import _check_calling_me_nickname

import hoshino
from hoshino.service import sucmd
from hoshino.typing import CommandSession, CQHttpError
from hoshino import R, Service, util, priv
from hoshino.util import DailyNumberLimiter

sv = Service('anti-abuse', visible=False, manage_priv=priv.SUPERUSER)

crawl = DailyNumberLimiter(1)

BANNED_WORD = (
	'rbq', 'RBQ', '憨批', '废物', '死妈', '崽种', '傻逼', '傻逼玩意',
	'没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', 'cnm', 'kkp',
	'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬', '滚',
	'给爷滚', '给老子滚', '给老子爬'
)

def get_sec(tstr):

	hour,minute,second = 0,0,0
	try:
		if "小时" in tstr:
			splt = tstr.split("小时")
			hour = int(splt[0])
			tstr = splt[1]
		if "分钟" in tstr:
			splt = tstr.split("分钟")
			minute = int(splt[0])
			tstr = splt[1]
		if "秒" in tstr:
			splt = tstr.split("秒")
			second = int(splt[0])
			tstr = splt[1]
	except Exception as e:
		return e

	return (hour,minute,second)

async def process(bot, event):
	user_id = event['user_id']
	msg_from = str(user_id)
	if event['message_type'] == 'group':
		group_id=event["group_id"]
	elif event['message_type'] == 'discuss':
		group_id=event["discuss_id"]
	else:
		group_id = None

	if (group_id is not None and priv.check_block_group(group_id)) or priv.check_block_user(user_id):
		return

	hoshino.priv.set_block_user(user_id, timedelta(hours=1))
	pic = R.img(f"angry.jpg").cqcode
	await bot.send(event,f"不理你啦！バーカー\n{pic}", at_sender=True)
	#await util.silence(event, 1*60*60)

@on_command('ban_word', aliases=BANNED_WORD, only_to_me=True)
async def ban_word(session):
	event = session.event
	bot = session.bot
	await process(bot,event)

@sv.on_fullmatch(('爬','爪巴'),only_to_me=True)
async def tolerable_ban_word(bot,event):
	uid = event['user_id']
	if crawl.check(uid):
		crawl.increase(uid)
		await bot.send(event,'别骂了别骂了，我爬就是了……再骂就不理你了！',at_sender=True)
	else:
		crawl.reset(uid)
		await process(bot,event)

@sv.on_prefix(('拉黑用户','拉黑群员','拉黑群友'))
async def block_user(bot,event):

	if event.user_id not in bot.config.SUPERUSERS:
		return

	message = event.message
	param = message.extract_plain_text()
	delta = get_sec(param)
	if isinstance(delta,Exception):
		await bot.send(event,f"参数错误：{str(delta)}")
		return
	if delta == (0,0,0):
		delta = (8,0,0)
	suspend = timedelta(hours=delta[0],minutes=delta[1],seconds=delta[2])

	count = 0
	for m in message:
		if m.type == 'at' and m.data['qq'] != 'all':
			uid = int(m.data['qq'])
			priv.set_block_user(uid,suspend)
			count += 1

	if count > 0:
		msg = f"已拉黑{count}位用户"
		if delta[0]>0:
			msg += f"{delta[0]}小时"
		if delta[1]>0:
			msg += f"{delta[1]}分钟"
		if delta[2]>0:
			msg += f"{delta[2]}秒"
		await bot.send(event,msg,at_sender=True)
	else:
		await bot.send(event,"没有用户被拉黑",at_sender=True)

@sv.on_prefix(('拉黑本群','拉黑群'))
async def block_group(bot,event):

	if event.user_id not in bot.config.SUPERUSERS:
		return

	message = event.message
	param = message.extract_plain_text()
	delta = get_sec(param)
	if isinstance(delta,Exception):
		await bot.send(event,f"参数错误：{str(delta)}",at_sender=True)
		return
	if delta == (0,0,0):
		delta = (8,0,0)
	suspend = timedelta(hours=delta[0],minutes=delta[1],seconds=delta[2])

	gid = event.group_id
	priv.set_block_group(gid,suspend)

	msg = f"已拉黑本群"
	if delta[0]>0:
		msg += f"{delta[0]}小时"
	if delta[1]>0:
		msg += f"{delta[1]}分钟"
	if delta[2]>0:
		msg += f"{delta[2]}秒"
	await bot.send(event,msg,at_sender=True)

@sv.on_prefix(('取消拉黑用户','解除拉黑用户','取消拉黑群员','解除拉黑群员','取消拉黑群友','解除拉黑群友'))
async def unblock_user(bot,event):

	if event.user_id not in bot.config.SUPERUSERS:
		return

	message = event.message
	count = 0
	for m in message:
		if m.type == 'at' and m.data['qq'] != 'all':
			uid = int(m.data['qq'])
			priv.set_block_user(uid,timedelta(seconds=0))
			count += 1

	if count>0:
		msg = f"已解除{count}位用户的拉黑"
	else:
		msg = "没有用户被解除拉黑"

	await bot.send(event,msg,at_sender=True)

@on_command('取消拉黑本群',aliases=('解除拉黑本群','取消拉黑此群','解除拉黑此群'),only_to_me=False)
async def unblock_group(session):
	event = session.event
	uid = event['user_id']
	if event['message_type'] == 'group':
		gid=event["group_id"]
	elif event['message_type'] == 'discuss':
		gid=event["discuss_id"]
	else:
		return

	if uid not in session.bot.config.SUPERUSERS:
		return

	priv.set_block_group(gid,timedelta(seconds=0))
	await session.send("已解除本群拉黑",at_sender=True)