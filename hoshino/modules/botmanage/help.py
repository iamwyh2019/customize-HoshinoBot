from hoshino import Service, priv, config
from hoshino.typing import CQEvent

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

botname = config.BOTNAME

TOP_MANUAL = f'''
发送方括号[]内的关键词即可触发

[怎么拆日和] 竞技场查询
[{botname}来发十连] 转蛋模拟
[切噜一下] 切噜语转换

更多功能：
[帮助pcr查询]
[帮助pcr娱乐]
[帮助pcr会战]
'''.strip()

def gen_bundle_manual(bundle_name, service_list, gid):
    manual = ['发送方括号[]内的关键词即可触发，不需要输入方括号[]或尖括号<>，加号+用空格代替']
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible and sv.check_enabled(gid):
            spit_line = '=' * max(0, 18 - len(sv.name))
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name} {spit_line}")
            if sv.help:
                manual.append(sv.help)
    return '\n'.join(manual)


@sv.on_prefix(('help', '帮助', '幫助'))
async def send_help(bot, ev: CQEvent):
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    if not bundle_name:
        await bot.send(ev, TOP_MANUAL)
    elif bundle_name in bundles:
        msg = gen_bundle_manual(bundle_name, bundles[bundle_name], ev.group_id)
        await bot.send(ev, msg)
    # else: ignore
