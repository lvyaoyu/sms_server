# -*- coding: utf-8 -*-
# @Time : 2022-12-06 16:51 
# @Author : YD

from fastapi import APIRouter, Request

from app.extensions.resp_ext import resp_200
from app.schemas.sign_schema import SignData
from app.extensions.sign_ext import generate_sign
from app.tools.common_tool import get_timestamp

sign_app = APIRouter()


@sign_app.post('/create')
async def create_sign(
        request: Request,
        data: SignData,
):
    timestamp = get_timestamp()
    sign = await generate_sign(timestamp, data.secret)
    data = {
        'sign':sign,
        'timestamp':timestamp,
    }
    return resp_200(request, data)
