# -*- coding: utf-8 -*-
# @Time : 2022-12-06 16:54 
# @Author : YD
from pydantic import BaseModel, Field


class SignData(BaseModel):
    secret: str = Field(..., description='密钥')
    # timestamp: str = Field(..., description='时间戳')
