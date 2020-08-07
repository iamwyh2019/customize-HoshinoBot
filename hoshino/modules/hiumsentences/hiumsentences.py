import requests
from hoshino import Service
from hoshino.typing import CommandSession

sv = Service('hiumsentences', enable_on_default=True, visible=True)

@sv.on_command('网抑云时间', aliases=('上号','生而为人','生不出人','网抑云','已黑化'), only_to_me=True)
async def music163_sentences(session: CommandSession):
    resp = requests.get('http://api.heerdev.top/nemusic/random',timeout=5)
    if resp.status_code == requests.codes.ok:
        res = resp.json()
        sentences = res['text']
        await session.send(sentences, at_sender=True)
    else:
        await session.send('上号失败，我很抱歉。查询出错，请稍后重试。', at_sender=True)