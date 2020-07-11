import random,os
import hoshino
from hoshino import Service, R
from hoshino.typing import CQEvent
from hoshino.util import DailyNumberLimiter

sv = Service('pcr-login-bonus', bundle='pcr娱乐', help_='[优妮签到] 给主人盖章章')

lmt = DailyNumberLimiter(1)
login_presents = [
    '扫荡券×5',  '卢币×1000', '普通EXP药水×5',  '宝石×50',  '玛那×3000',
    '扫荡券×10', '卢币×1500', '普通EXP药水×15', '宝石×80',  '白金转蛋券×1',
    '扫荡券×15', '卢币×2000', '上级精炼石×3',   '宝石×100', '白金转蛋券×1',
]
todo_list = [
    '找伊绪老师上课',
    '给宫子买布丁',
    '和真琴寻找伤害优衣的人',
    '找镜哥探讨女装',
    '跟吉塔一起登上骑空艇',
    '和霞一起调查伤害优衣的人',
    '和佩可小姐一起吃午饭',
    '找小小甜心玩过家家',
    '帮碧寻找新朋友',
    '去真步真步王国',
    '找镜华补习数学',
    '陪胡桃排练话剧',
    '和初音一起午睡',
    '成为露娜的朋友',
    '帮铃莓打扫咲恋育幼院',
    '和静流小姐一起做巧克力',
    '去伊丽莎白农场给栞小姐送书',
    '观看慈乐之音的演出',
    '解救挂树的队友',
    '来一发十连',
    '井一发当期的限定池',
    '给妈妈买一束康乃馨',
    '购买黄金保值',
    '竞技场背刺',
    '给别的女人打钱',
    '氪一单',
    '努力工作，尽早报答妈妈的养育之恩',
    '成为魔法少女',
    '搓一把日麻'
]

stampdir=os.path.abspath(os.path.join(hoshino.config.RES_DIR, "img/priconne/stamp"))
stamplst=os.listdir(stampdir)

# The stamp images are from https://tieba.baidu.com/p/6769790810. All rights reserved to the author.
# We sincerely thank him/her for his/her works.

@sv.on_fullmatch(('签到', '盖章', '妈', '妈?', '妈妈', '妈!', '妈！', '妈妈！'), only_to_me=True)
async def give_okodokai(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.send(ev, '明天再来吧~', at_sender=True)
        return
    lmt.increase(uid)
    present = random.choice(login_presents)
    todo = random.choice(todo_list)
    stamp = random.choice(stamplst)
    await bot.send(ev, f'\n主人欢迎回来{R.img("priconne/stamp/"+stamp).cqcode}\n获得了{present}\n这是我的小礼物\n主人今天要{todo}吗？', at_sender=True)

@sv.on_prefix('重置签到')
async def stamp_reset(bot, ev: CQEvent):
    if ev.user_id not in bot.config.SUPERUSERS:
        return
    count = 0
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            uid = int(m.data['qq'])
            lmt.reset(uid)
            count+=1
    if count:
        await bot.send(ev, f"已重置{count}位用户的签到状况。")

@sv.on_fullmatch('刷新印章库')
async def reload_stamp(bot, ev: CQEvent):
    if ev.user_id not in bot.config.SUPERUSERS:
        return
    global stampdir, stamplst
    stamplst=os.listdir(stampdir)
    await bot.send(ev, f"刷新成功，现在有{len(stamplst)}张印章图片。")