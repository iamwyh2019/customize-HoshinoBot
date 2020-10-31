from hoshino import Service, priv
import random

sv = Service('admin_box', visible=False)

@sv.on_prefix(('申请头衔',))
async def set_title(bot, event):
	uid = event.user_id
	gid = event.group_id
	title = event.message.extract_plain_text()
	await bot.set_group_special_title(group_id=gid, user_id=uid, special_title=title)

@sv.on_prefix(('设置群名',))
async def set_group_name(bot, event):
	if not priv.check_priv(event, priv.SUPERUSER):
		return
	gid = event.group_id
	name = event.message.extract_plain_text()
	await bot.set_group_name(group_id=gid,group_name=name)

@sv.on_fullmatch(('群地位',))
async def show_group_role(bot, event):
	if not priv.check_priv(event, priv.SUPERUSER):
		return
	me = await bot.get_login_info()
	gid = event.group_id
	uid = me['user_id']
	name = me['nickname']
	info = await bot.get_group_member_info(group_id=event.group_id, user_id=uid)
	role = info['role']
	await bot.send(event, f'{name}在此群的地位是{role}')

@sv.on_prefix(('戳一戳',),only_to_me=True)
async def poke(bot, event):
	if not priv.check_priv(event, priv.SUPERUSER):
		return
	uid = 0
	for msg in event.message:
		if msg.type == 'at' and msg.data['qq'] != 'all':
			uid = int(msg.data['qq'])
			break
	if uid == 0:
		await bot.send(event, '你想戳谁？', at_sender=True)
	else:
		await bot.send(event, f'[CQ:poke,qq={uid}]')

@sv.on_prefix(('送礼物',),only_to_me=True)
async def send_gift(bot, event):
	uid = 0
	for msg in event.message:
		if msg.type == 'at' and msg.data['qq'] != 'all':
			uid = int(msg.data['qq'])
			break
	if uid == 0:
		await bot.send(event, '你想送给谁？', at_sender=True)
	else:
		await bot.send(event, f'[CQ:gift,qq={uid},id={random.randint(0,8)}]')

'''
@sv.on_notice('group_recall')
async def show_recall(session):
	bot,event=session.bot,session.event
	if event.user_id != event.operator_id:
		return
	mid = event.message_id
	uid = event.user_id
	msg = await bot.get_group_msg(message_id=mid)
	msg = msg['content']
	await bot.send(event, f'[CQ:at,qq={uid}]撤回的消息是：\n{msg}')
'''
anti_anony = ('你是谁？','为什么要匿名？')
@sv.on_message('group')
async def anti_anonymous(bot, event):
	if not event.anonymous:
		return
	await bot.send(event, random.choice(anti_anony))