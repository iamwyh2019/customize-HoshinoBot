import random

from nonebot import on_command

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('在啊。')

sv = Service('chat', visible=False)

@sv.on_keyword(('沙雕机器人', '沙雕機器人', '笨蛋机器人', '傻逼机器人', '憨憨机器人', '憨批机器人', 'sb机器人', 'バカ机器人',
    '沙雕优妮','笨蛋优妮','傻逼优妮','憨憨优妮','憨批优妮','sb优妮','バカ优妮'))
async def say_sorry(bot, ev):
    await bot.send(ev, '你在说谁？')

@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, '大庭广众的，别这么肉麻。')

@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '人不能，至少不应该。', at_sender=True)

@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, '滚！', at_sender=True)
    else:
        await bot.send(ev, '大庭广众的，别这么肉麻。')

@sv.on_fullmatch(('我登顶了','我挖完了', '我到顶了', '我出货了'), only_to_me=True)
async def chat_congrat(bot, ev):
    await bot.send(ev, '恭喜！', at_sender=True)

@sv.on_fullmatch(('我井了','我天井了', '我沉了'), only_to_me=True)
async def chat_sympathy(bot, ev):
    if random.random()<0.95:
        await bot.send(ev, '真可惜。不过不要灰心，说不定下一次抽卡就出奇迹了呢！', at_sender=True)
    else:
        await bot.send(ev, '真的吗？好可怜…噗哈哈哈…', at_sender=True)

@sv.on_fullmatch(('我好了','我有个朋友说他好了', '我朋友说他好了'))
async def nihaole(bot, ev):
    if random.random() <= 0.50:
        await bot.send(ev, '不许好，憋回去！')
        await util.silence(ev, 30)

@sv.on_fullmatch(('晚安','晚安哦', '晚安啦', 'good night', 'gn'), only_to_me=True)
async def goodnight(bot, ev):
    await bot.send(ev, '晚安~', at_sender=True)
'''
@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    await util.silence(ev, 30)
'''

# ============================================ #

@sv.on_keyword(('涩图', 'setu', '色图', '黄图', 'h图'))
async def chat_antisetu(bot, ctx):
    if random.random() < 0.15:
        await bot.send(ctx, '不要ghs哦。')

@sv.on_keyword(('大佬', 'dalao', '大神'))
async def chat_dalao(bot, ctx):
    if random.random() < 0.15:
        await bot.send(ctx, R.img('dalao.jpg').cqcode)

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.15:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('我的天啊你看看都几点了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.15:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

nyb_player = f'''正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.15:
        await bot.send(ev, nyb_player)
