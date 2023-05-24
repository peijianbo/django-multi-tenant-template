#!/bin/bash
# !!! 需要先手工login hub

docker build -f Dockerfile -t itom_project:1.0.0 .
# 重命名镜像
docker tag itom_project:1.0.0 tyhub.touch4.me/ops/itom_project:1.0.0
# 推送镜像
docker push tyhub.touch4.me/ops/itom_project:1.0.0
