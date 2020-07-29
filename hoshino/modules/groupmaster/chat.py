import random

from nonebot import on_command
from datetime import datetime
import pytz

import hoshino
from hoshino import R, Service, priv, util

tz = pytz.timezone('Asia/Shanghai')

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('在啊。')

sv = Service('chat', visible=False)

@sv.on_keyword(('沙雕机器人', '笨蛋机器人', '傻逼机器人', '憨憨机器人', 
    '憨批机器人', '沙雕优妮','笨蛋优妮','傻逼优妮','憨憨优妮','憨批优妮'))
async def chat_sad(bot, ev):
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

@sv.on_fullmatch(('晚安','晚安哦', '晚安啦', 'good night'), only_to_me=True)
async def goodnight(bot, ev):
    now_hour=datetime.now(tz).hour
    if now_hour<=3 or now_hour>=21:
        await bot.send(ev, '晚安~', at_sender=True)
    elif 19<=now_hour<21:
        await bot.send(ev, f'现在才{now_hour}点，这么早就睡了吗？', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没到晚上咧。嘿嘿。', at_sender=True)

@sv.on_fullmatch(('晚上好','晚上好啊', '晚上好呀', 'good evening'), only_to_me=True)
async def goodevening(bot, ev):
    now_hour=datetime.now(tz).hour
    if 18<=now_hour<24:
        await bot.send(ev, f'晚上好！今晚想做什么呢？', at_sender=True)
    elif 0<=now_hour<6:
        await bot.send(ev, f'{now_hour}点啦，还不睡吗？', at_sender=True)
    elif 6<=now_hour<=9:
        await bot.send(ev, f'晚上好…嗯？我刚起床呢。', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没天黑呢。嘿嘿。', at_sender=True)

@sv.on_fullmatch(('你真棒','你好棒','你真厉害','你好厉害'), only_to_me=True)
async def iamgood(bot, ev):
    await bot.send(ev, f'诶嘿嘿~')

@sv.on_fullmatch(('早安','早安哦', '早上好', '早上好啊', '早上好呀', '早', 'good morning'), only_to_me=True)
async def goodmorning(bot, ev):
    now_hour=datetime.now(tz).hour
    if 0<=now_hour<6:
        await bot.send(ev, f'好早，现在才{now_hour}点呢。', at_sender=True)
    elif 6<=now_hour<10:
        await bot.send(ev, '早上好！今天打算做什么呢？', at_sender=True)
    elif 21<=now_hour<24:
        await bot.send(ev, '别闹，准备睡觉啦。', at_sender=True)
    else:
        await bot.send(ev, f'{now_hour}点了才起床吗…', at_sender=True)

@sv.on_fullmatch(('你是谁','你是谁啊', '你是谁？', '你是谁啊？', '你是谁?', '你是谁啊?'), only_to_me=True)
async def selfintro(bot, ev):
    await bot.send(ev,'我是圣特蕾莎女子学院好朋友部的优妮～')

hentai_audio=("你是变态可疑分子.mp3","我懂了，你是变态吧.m4a")
roar_audio=("瓜啊.m4a","呜啊.m4a")

@sv.on_fullmatch(('变态','我是变态','我是绅士','变态可疑分子','可疑分子'))
async def chat_hentai(bot,ev):
    rec=random.choice(hentai_audio)
    await bot.send(ev,R.rec(rec).cqcode)

@sv.on_fullmatch(('娇喘',))
async def chat_roar(bot,ev):
    rec=random.choice(roar_audio)
    await bot.send(ev,R.rec(rec).cqcode)

@sv.on_fullmatch(('唱歌','唱首歌','来首歌','来唱首歌'), only_to_me=True)
async def sing(bot,ev):
    await bot.send(ev,R.rec('song.mp3').cqcode)

@sv.on_fullmatch(('再见','拜拜'),only_to_me=True)
async def farewell(bot,ev):
    await bot.send(ev,"拜拜~",at_sender=True)

# ============================================ #

@sv.on_keyword(('吃优妮'))
async def eatme(bot, ev):
    await bot.send(ev, '这样不好。真的。', at_sender=True)

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


#@sv.on_keyword(('伊莉亚','伊利亚','伊莉雅','伊利雅','yly'))
#async def chat_yly(bot, ctx):
#    if random.random() < 0.15:
#        await bot.send(ctx, f'''伊莉亚，嘿嘿嘿\n{R.img('伊莉亚.gif').cqcode}''')

#nyb_player = f'''{R.img('春黑.gif').cqcode}
#正在播放：New Year Burst
#──●━━━━ 1:05/1:30
#⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
#'''.strip()

#@sv.on_keyword(('春黑', '新黑'))
#async def new_year_burst(bot, ev):
#    if random.random() < 0.15:
#        await bot.send(ev, nyb_player)
