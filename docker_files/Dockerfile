FROM tyhub.touch4.me/ops/tyops-django:0.0.1

LABEL maintainer="peijianbo <peijianbo@tuyoogame.com>"
LABEL description="itom_project-backend"

COPY requirements.txt /data/server/
COPY run /data/server/run/

RUN pip install -U pip && \
    pip install --default-timeout=60 --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /data/server/requirements.txt

EXPOSE 8000

CMD ["sh","/data/server/run/start.sh"]