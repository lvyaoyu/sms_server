# -*- coding: utf-8 -*-
# @Time : 2022-04-14 13:37 
# @Author : YD

import os
from pydantic import BaseSettings


class Setting(BaseSettings):
    cache_ttl = 60 * 5


class DEVSetting(Setting):
    redis_host = ''

    redis_port = 16379

    redis_database = 0

    redis_username = ''

    redis_password = ''

    secret = '123'
    secret_ttl = 60 * 120


class TestSetting(Setting):
    redis_host = ''

    redis_port = 16379

    redis_database = 0

    redis_username = ''

    redis_password = ''


class PROSetting(Setting):
    redis_host = ''

    redis_port = 16379

    redis_database = 0

    redis_username = ''

    redis_password = ''


ENV = os.environ.get('ENV')
if ENV == 'PRO':
    print('生产环境')
    setting = PROSetting()
elif ENV == 'Test':
    print('测试环境')
    setting = TestSetting()
else:
    print('开发环境')
    setting = DEVSetting()

for k, v in setting.dict().items():
    print(f'{k}:{v}')
