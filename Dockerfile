FROM python:3.8.5
LABEL maintainer="lvyaoyu@uniner.com"
USER root

ENV LC_ALL=C.UTF-8 \
    LANG=zh_CN.UTF-8 \
    DISPLAY=:1.0 \
    TZ=Asia/Shanghai

WORKDIR /root/code

COPY ./requirements.txt /root/code/requirements.txt


RUN pip config set global.index-url https://pypi.douban.com/simple/ \
    && python3 -m pip install --upgrade pip\
    && pip install wheel \
    && pip install --no-cache-dir --upgrade -r /root/code/requirements.txt

COPY . /root/code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--log-config", "LOGGING_CONFIG.json"]