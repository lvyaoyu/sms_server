# -*- coding: utf-8 -*-
# @Time : 2021-12-03 20:04 
# @Author : YD
import re
import time

from hashlib import md5
from typing import List, Union, Literal, Optional


def get_md5(str_: str, charset="utf-8"):
    md5_str = md5(str_.encode(encoding=charset)).hexdigest()
    return md5_str


def data_strip(
        l: Union[str, List[str]],
        return_type: Literal['str', 'list'] = 'str',
        sep='',
) -> Union[None, str, List[str]]:
    if isinstance(l, list):
        if return_type == 'list':
            return [re.sub('\s+', ' ', i).strip() for i in l if re.sub('\s+', ' ', i).strip()]
        else:
            return re.sub('\s+', ' ', sep.join(l)).strip()
    elif isinstance(l, str):
        return re.sub('\s+', ' ', l).strip()


def get_timestamp(return_type: Literal['str', 'int'] = 'str'):
    """得到13位时间戳"""
    millis = int(round(time.time() * 1000))
    return millis if return_type == 'int' else str(millis)


def timestamp_to_time(millis):
    """13位时间戳转换为日期格式字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(millis / 1000))


def read_file(file_path, mode: Literal['r', 'rb', 'r+']):
    with open(file_path, mode=mode, encoding='utf-8') as f:
        text = f.read()
    return text
