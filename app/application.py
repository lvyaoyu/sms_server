# -*- coding: utf-8 -*-
# @Time : 2022-04-14 15:56 
# @Author : YD
import time

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from cacheout import Cache

from app.api.sms_api import sms_app
from app.api.sign_api import sign_app
from app.extensions.logger_ext import logger
from app.extensions.resp_ext import resp_500

from app.config import setting


def _register_route(app: FastAPI) -> None:
    # 整合各模块路由
    app.include_router(sms_app, prefix="/sms", tags=['SMS'])
    # app.include_router(sign_app, prefix="/sign", tags=['SIGN'])


def _register_cors(app: FastAPI) -> None:
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    # 可跨域访问的基本请求设置
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _register_middleware(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        try:
            response = await call_next(request)
            return response
        except BaseException as e:
            return resp_500(request, e)
        finally:
            process_time = time.time() - start_time
            logger.debug('接口耗时：{:2f}s'.format(process_time))


def _register_cache(app: FastAPI):
    @app.on_event("startup")
    async def startup_connect():
        app.state.cache = Cache(
            ttl=setting.cache_ttl
        )

    @app.on_event('shutdown')
    async def shutdown_connect():
        app.state.cache.clear()


def _create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="SMS",
        version="1.0.0",
        docs_url="/v1/docs"
    )
    # 注册路由
    _register_route(app)
    # 注册跨域
    _register_cors(app)
    # 注册中间件
    _register_middleware(app)
    # 注册缓存
    _register_cache(app)

    return app


app = _create_app()

__all__ = ['app']
