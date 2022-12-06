# -*- coding: utf-8 -*-
# @Time : 2022-03-31 22:44 
# @Author : YD

import aioredis
from aioredis import Redis
from app.config import setting

"""
For example::

    redis://[[username]:[password]]@localhost:6379/0
    rediss://[[username]:[password]]@localhost:6379/0
    unix://[[username]:[password]]@/path/to/socket.sock?db=0
"""
if setting.redis_username and setting.redis_password:
    _redis_url = f"redis://[[{setting.redis_username}]:[{setting.redis_password}]]{setting.redis_host}:{setting.redis_port}/{setting.redis_database}"
elif setting.redis_username:
    _redis_url = f"redis://[[{setting.redis_username}]:[]]{setting.redis_host}:{setting.redis_port}/{setting.redis_database}"
elif setting.redis_password:
    _redis_url = f"redis://[[]:[{setting.redis_password}]]{setting.redis_host}:{setting.redis_port}/{setting.redis_database}"
else:
    _redis_url = f"redis://{setting.redis_host}:{setting.redis_port}/{setting.redis_database}"

print(_redis_url)

_Redis_Pool = aioredis.ConnectionPool.from_url(
    _redis_url,
    max_connections=10,
    decode_responses=True
)


def create_redis() -> Redis:
    redis = aioredis.Redis(connection_pool=_Redis_Pool)
    return redis

__all__ = ['create_redis']
