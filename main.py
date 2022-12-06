# -*- coding: utf-8 -*-
# @Time : 2022-09-16 18:53 
# @Author : YD

import uvicorn

from app.application import app

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8080, reload=True, debug=True, log_config="LOGGING_CONFIG.json")
