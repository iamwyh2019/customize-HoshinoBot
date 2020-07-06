from hoshino import Service

sv_help = '''
[谁是霸瞳] 角色别称查询
'''.strip()

sv = Service('pcr-query', help_=sv_help, bundle='pcr查询')

from .query import *
from .whois import *
from .miner import *
