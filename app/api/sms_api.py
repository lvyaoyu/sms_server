# -*- coding: utf-8 -*-
# @Time : 2022-10-09 16:15 
# @Author : YD

from typing import Optional

from fastapi import APIRouter, Request, Query, Depends

from app.extensions.resp_ext import resp_200
from app.extensions.logger_ext import logger
from app.extensions.sign_ext import verify_headers
from app.schemas.sms_schema import SMSData

sms_app = APIRouter(
    dependencies=[Depends(verify_headers)]
)


# @sms_app.post('/msg/receive/{key}')
# async def receive_msg(
#         request: Request,
#         key: str = Path(..., description='redis字符串key'),
#         value: Dict[str, str] = Body(None, description='发送的消息体'),
#         cache_time: Optional[int] = 60 * 5,
#         _redis: Redis = Depends(create_redis),
# ):
#     print(await request.body())
#     v = value.get('value')
#     set_result = await _redis.set(key, v)
#     if not set_result:
#         raise Exception(f'set {key} error')
#     expire_result = await _redis.expire(key, cache_time)
#     logger.info(f'redis expire {key} result:{expire_result}')
#     if not expire_result:
#         raise Exception(f'expire {key} {cache_time} error')
#     return resp_200(request, set_result)
#
#
# @sms_app.get('/msg/send/{key}')
# async def receive_msg(
#         request: Request,
#         key: str = Path(..., description='redis字符串key'),
#         _redis: Redis = Depends(create_redis),
# ):
#     result = await _redis.get(key)
#     return resp_200(request, result)


@sms_app.post('/msg/receive')
async def receive_msg(
        request: Request,
        sms_data: SMSData,
        cache_time: Optional[int] = None,
):
    logger.debug(sms_data)
    if cache_time:
        request.app.state.cache.set(sms_data.phone, sms_data.sms_info, ttl=cache_time)
    else:
        request.app.state.cache.set(sms_data.phone, sms_data.sms_info)

    return resp_200(request, True)


@sms_app.get('/msg/query')
async def receive_msg(
        request: Request,
        phone: Optional[str] = Query(None, description='手机号'),
):
    if phone:
        if not request.app.state.cache.has(phone):
            result = {}
        else:
            result = {phone: request.app.state.cache.get(phone)}
    else:
        result = dict(request.app.state.cache.items())
    return resp_200(request, result)
