FROM ubuntu:18.04

RUN sed -i "s/archive.ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list

RUN sed -i "s/security.ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list

RUN apt-get update && apt-get install -y python3 python3-pip nginx

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple tornado==5.1.1 \
    casbin>=0.2 \
    requests>=2.22.0 \
    pymongo>=3.7.2 \
    defaultlist \
    pycrypto \
    pytz \
    IPy


COPY nginx.conf /etc/nginx/nginx.conf
# COPY frontend /frontend
COPY src /src

WORKDIR /src

CMD ["python3", "run.py"]