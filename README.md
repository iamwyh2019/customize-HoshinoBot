# HoshinoBot (customized)

HoshinoBot�ĸ����޸İ档��װ�Ͳ���ָ���뿴[����](#deploy)��

����Ŀ���ṩԭ��Ŀ����Դ�ļ�����ǰ��HoshinoBotԭ[��Ŀ��ַ](https://github.com/Ice-Cirno/HoshinoBot)������Դ�ļ����������Դ�ļ���res�ļ����У����ܲ����������������issue��ȡδ�ϴ�����Դ��

**2021��1��5�յĸ����޸��˻����������ļ��ṹ�����ϴ�����Ӧ��ʾ�������ļ���������ǰʹ�ù�����Ŀ�Ĵ��룬��μ�����[20210105����](#botname����)�����Ļ����������ļ�������Ӧ�޸ģ��Ա��ⲻ��Ҫ�Ĵ�����������֮��ſ�ʼ������ֻ��Ҫ������Ŀ�е�ʾ�������ļ����ɣ�����Ҫ�޸ġ�**

<a href="#botname%E6%9B%B4%E6%96%B0">testlink</a>

## ���

����Ŀ��ԭ������˽����������޸ģ���Щ�޸Ŀ��ܵ�����ԭ������˲��ֹ��ܲ����ݡ��޸İ�����

- ��[���Ͽ�](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/groupmaster/chat.py)�м������Ӧ��
- ��[��Դ��ӿ�](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/R.py)�����`ResRec`���Դ���������
- ��[�㲥](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/botmanage/broadcast.py)����ӡ�����Ⱥ����Ϣ�����ܣ��÷���˽��������`gbc [Ⱥ��] [����]`��
- **������**���޸�[ÿ��ǩ��](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/priconne/login_bonus.py)����ӡ��ͼƬ��λ�ã�֧��ӡ��ͼƬ�����ȸ��£���������ǩ������Ĺ��ܡ������ݵ�ԭ�����޸���ӡ��·����
- ��[������](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/groupmaster/anti_abuse.py)�м�����������ĳ���˻�ĳ��Ⱥ����������ڣ��Ĺ��ܣ�
- ����[��ɫ���ݿ�](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/priconne/_pcr_data.py)�����ݣ�
- **������**������ս�ڼ�[hourcall](https://github.com/iamwyh2019/customize-HoshinoBot/blob/master/hoshino/modules/hourcall/hourcall.py)��ʹ��һ��ר����Թ���ս���İ���ͬʱ��������ֶ�������ʱ���ܣ�������ԡ������ݵ�ԭ�������İ��ļ��м��뵱�ڹ���ս�����ڣ��ڶ���ԭ���İ�ʱ����Ϊ�����������Ϣ������
- �޸�[����ս����ϵͳ](https://github.com/iamwyh2019/customize-HoshinoBot/blob/master/hoshino/modules/pcrclanbattle/clanbattle/cmdv2.py)�������������ܣ�ȡ���������ܣ�֧��ԤԼ����������ʹ�������鵶���ĵ����ܸ��Ӿ�ϸ���ã�

ͬʱ����д��װ�����ɲ����������

- ��ѯ����ս������[��Ŀ��ַ](https://github.com/pcrbot/clanrank)
- ��ѯ��顢���ܡ�ר����Ϣ��[��Ŀ��ַ](https://github.com/pcrbot/pcr-wiki)
- �鿴�ճ̱�[��Ŀ��ַ](https://github.com/pcrbot/schedule)
- ��ҳ���������������`view.py`���ں��������û���ϴ�����ο�`/hoshino/modules/botmanage/web_service_manager`��README�������ã�
- Ⱥ�յ���
- ������������
- ����ս��ְ���棻

��Щ���������Ȩ����ԭ���ߣ�����GPL-v3Э�鿪Դ��

����֮�⣬����Ŀ�����˲��ֲ������޸Ľӿڣ�ʵ�ֲ����ȸ��£�������

- ����ÿ��ǩ�����
- ����ӡ�¿����ӡ���б�
- ���ò�ѯ��ʱ��ʾ�������ҵ��

����ĸ������ݿɲ���commit��

## ��Դ

����Ŀ��GPL-v3Э�鿪Դ�����������⸴�ơ�ʹ�á��޸ġ���������Ʒ��������Ʒ������Ҫ��ǿ����߷ַ���Щ��Ʒ������Ҫ��GPL-v3Э�鿪Դ���������Ķ�[��ԴЭ��](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/LICENSE)��

<h2 id="deploy"> ���� </h2>

�����ṩ��һ��ʾ�������ļ���λ��`hoshino/config_example`�ļ����С������ر���Ŀ���룬**������ļ������ָ�Ϊ`config`**����д`__bot__.py`����Щ�ֶΣ�

```python
PORT = 8080   # hoshino�����Ķ˿���ip
#HOST = '127.0.0.1'      # Windows����ʹ�ô�������
HOST = '0.0.0.0'   # linux + dockerʹ�ô�������

SUPERUSERS = []    # ��д�����û��������˹���Ա����QQ�ţ��������ð�Ƕ���","����
NICKNAME = ()           # �����˵��ǳơ������ǳƵ�ͬ��@bot������Ԫ�����ö���ǳ�
BOTNAME = ''  # �����˵�����

RES_PROTOCOL = 'file'
RES_DIR = r'/res'  # ��Դ���ļ��У���ɶ���д��windows��ע�ⷴб��ת��
RES_URL = 'http://172.17.0.1:8080/res/'   # ʹ��httpЭ��ʱ����д��ԭ���ϸ�urlӦָ��RES_DIRĿ¼
```

�밴���ķ������ͻ�����ʵ����������޸ģ�����ɼ��ļ��ڴ���ע�͡�

**��ѡ**����`hoshino/config/priconne.py`�����뾺������ѯkey����������ѯ���ܵ��������� [��������Re: Dive Fan Club - Ӳ�˵ľ��������ݷ���վ](https://pcrdfans.com/) ����ѯ��Ҫ��Ȩkey����������pcrdfans��������Ҫ����ע��������������˴�߽϶࣬���߳������ţ�����**������**����ϵ�����Ƽ���ǰ����վ���в�ѯ��

�����go-cqhttp��[��Ŀ��ַ](https://github.com/Mrs4s/go-cqhttp/releases)���ط�����ϵͳ�ĳ��򣬲��ο�[���ý̳�](https://github.com/Mrs4s/go-cqhttp/blob/master/docs/config.md)����`config.ini`���������У���ر�`http_config`��`ws_config`������`ws_reverse_servers`������`reverse_url`�ĸ�ʽΪ`ws://[����IP]:[���ļ����˿�]/ws/`�������˿���HoshinoBot�ļ����˿ڱ���һ�¡�

���������������HoshinoBot��go-cqhttp��������˷��͡�bot���������лظ�����ɹ���

<h2 id="botname����"> 20210105���� </h2>

������`/hoshino/config/__bot__.py`�м����˱�ʾ���������ֵı�����

```python
BOTNAME = '����'
```

**�������Ļ����˵�`__bot__.py`������λ�ü�����һ�д��룬�������ָ�Ϊ�������˵����֡�**

��һ�Ķ�ּ�ڷ�����Ǩ�ƺʹ��ģ���������ʱ���ٸ����ڲ��İ������磬��Ϊ�����ݡ��Ļ����˿����ж�����硰��������������ʹ�÷�������������ʮ������Ӧ�����½�һ����Ϊ���������Ļ�����ʱ��ֻ��Ҫ�޸������ļ�����һ�м�����������İ��޸ġ�

������д�Լ��Ĳ��ʱ������ͷ��������һ�д��룺

```python
from hoshino.config import BOTNAME as botname  # ��botname������ϲ���ı�����
```

���������Ҫ�ἰ���������ֵĵط����øñ�����ʾ�����磺

```python
return f'{botname}��⵽������Ϊ��'
```

