# -*- coding: utf-8 -*-
# @Time : 2022-12-06 14:05 
# @Author : YD
from typing import Optional
from pydantic import BaseModel, Field


class SMSData(BaseModel):
    phone: str = Field(..., description='手机号')
    sms_info: str = Field(..., description='短信内容')


