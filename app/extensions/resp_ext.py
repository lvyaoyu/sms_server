# -*- coding: utf-8 -*-
# @Time : 2021-12-15 9:41 
# @Author : YD
from typing import Any
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.extensions.logger_ext import logger


def resp_200(
        request: Request,
        data: Any = None,
        message: str = "Success",
        code: int = 200
) -> JSONResponse:
    logger.debug(f'{request.client.host}:{request.client.port} "{request.method}" {request.url.path}?{request.url.query}\n{data}')
    return JSONResponse(
        status_code=200,
        content={
            'code': code,
            'message': message,
            'result': data
        }
    )


def resp_500(
        request: Request,
        error: Any = None,
        message: str = "Error",
        code: int = 500
) -> JSONResponse:
    if isinstance(error, Exception):
        error = error.__str__()

    logger.error(f'{request.client.host}:{request.client.port} "{request.method}" {request.url.path}?{request.url.query}\n{error}')

    return JSONResponse(
        status_code=200,
        content={
            'code': code,
            'message': message,
            'error': error
        }
    )
