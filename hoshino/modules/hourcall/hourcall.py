import pytz
from datetime import datetime
import hoshino
from hoshino import Service
from hoshino.service import sucmd
from hoshino.typing import CommandSession

sv = Service('hourcall', enable_on_default=False, help_='时报')
tz = pytz.timezone('Asia/Shanghai')

def get_hour_call():
    """挑出一组时报，每日更换，一日之内保持相同"""
    cfg = hoshino.config.hourcall
    now = datetime.now(tz)

    st,en = cfg.CLAN_BATTLE_DATE
    st = datetime.strptime(st,"%Y/%m/%d %H:%M:%S").replace(tzinfo=tz)
    en = datetime.strptime(en,"%Y/%m/%d %H:%M:%S").replace(tzinfo=tz)
    if st<=now<=en:
        return cfg.HOUR_CALLS["HOUR_CALL_CLANBATTLE"]
        
    hc_groups = cfg.HOUR_CALLS_ON
    g = hc_groups[ now.day % len(hc_groups) ]
    return cfg.HOUR_CALLS[g]


@sv.scheduled_job('cron', hour='*')
async def hour_call():
    now = datetime.now(tz)
    if 2 <= now.hour <= 4:
        return  # 宵禁 免打扰
    msg = get_hour_call()[now.hour]
    await sv.broadcast(msg, 'hourcall', 0)


@sucmd('manualhourcall', aliases=('mhc', '手动报时'))
async def manual_hourcall(session: CommandSession):
    msg = session.current_arg
    if msg!="":
        await sv.broadcast(msg, 'hourcall', 0)
    await hour_call()
