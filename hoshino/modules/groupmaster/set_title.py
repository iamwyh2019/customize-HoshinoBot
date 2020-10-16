from hoshino import Service, priv

sv = Service('设置头衔', visible=False)

@sv.on_prefix(('申请头衔',))
async def set_title(bot, event):
	uid = event.user_id
	gid = event.group_id
	title = event.message.extract_plain_text()
	await bot.set_group_special_title(group_id=gid,user_id=uid,special_title=title)

@sv.on_prefix(('设置群名',))
async def set_group_name(bot, event):
	if not priv.check_priv(event, priv.SUPERUSER):
		return
	gid = event.group_id
	name = event.message.extract_plain_text()
	await bot.set_group_name(group_id=gid,group_name=name)