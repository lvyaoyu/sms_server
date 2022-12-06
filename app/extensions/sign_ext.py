# -*- coding: utf-8 -*-
# @Time : 2022-12-06 16:23 
# @Author : YD
import base64
import hashlib
import hmac
import time
import urllib.parse
from typing import Optional

from fastapi import HTTPException, Header

from app.config import setting


async def verify_headers(
        sms: Optional[str] = Header(None)
):
    if sms != 'sms-2022':
        raise HTTPException(status_code=403, detail="Not authorized")


async def verify_sing(
        sign: Optional[str] = None,
        timestamp: Optional[str] = None,
):
    if not sign or not timestamp:
        raise HTTPException(status_code=403, detail="sign not match")

    if time.time() - int(timestamp) / 1000 > setting.secret_ttl:
        raise HTTPException(status_code=403, detail="sign failure")

    result = await generate_sign(timestamp, setting.secret)
    if sign != result:
        raise HTTPException(status_code=403, detail="sign not match")


async def generate_sign(timestamp, secret: str):
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return sign
