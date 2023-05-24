# ITOM
基于django框架实现的多租户架构方案
## 一、技术栈
```
Python==3.7.7
Django==3.2
DjangoRestFrameWork==3.12.4
```

## 二、目录结构
```
├── docker-compose.yml                        容器编排
├── docker_files                              镜像构建及启动
│   ├── Dockerfile
│   ├── build.sh
│   ├── requirements.txt
│   └── run                                   镜像启动
│       ├── start.sh
│       └── uwsgi.ini
└── itom_project                              项目根目录
    ├── __init__.py
    ├── itom_project                          项目同名子目录
    │   ├── __init__.py
    │   ├── apps                              应用模块目录
    │   │   ├── __init__.py
    │   │   └── organization                  组织架构应用模块
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations
    │   │       ├── models.py
    │   │       ├── serializers.py 
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   │   └── project                       项目应用模块
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations
    │   │       ├── models.py
    │   │       ├── serializers.py   
    │   │       ├── signals.py      
    │   │       ├── tasks.py            
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   │   └── record                         日志应用模块
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations
    │   │       ├── models.py
    │   │       ├── serializers.py    
    │   │       ├── signals.py         
    │   │       ├── tasks.py            
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   │   └── server                         与其他微服务交互的公共服务的模块
    │   │       └── micros
    │   │           ├── account.py        与用户系统通信
    │   │           └── cmdb.py           与cmdb系统通信
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations
    │   │       ├── models.py
    │   │       ├── serializers.py    
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── asgi.py
    │   ├── celery_app.py                      celery app配置中心
    │   ├── libs                               工具包
    │   │   ├── __init__.py
    │   │   ├── frameworks                     全局性、框架型工具包（如装饰器、中间件、mixins）
    │   │   │   ├── __init__.py
    │   │   │   ├── decorators.py
    │   │   │   ├── errors.py
    │   │   │   ├── exceptions.py
    │   │   │   ├── middlewares.py
    │   │   │   ├── mixins.py
    │   │   │   └── models.py
    │   │   └── utils                           常规工具包（如字符串处理、时间格式化）
    │   │       └── __init__.py
    │   ├── locale                              国际化支持
    │   │   └── en_us
    │   │       └── LC_MESSAGES
    │   │           ├── django.mo
    │   │           └── django.po
    │   ├── settings                            settings配置文件
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── db.py
    │   │   ├── dev.py
    │   │   ├── libs.py
    │   │   ├── prod.py
    │   │   ├── settings.py
    │   │   └── stg.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── logs                                    日志路径
    │   ├── itom_cmdb.log
    │   └── uwsgi.log
    ├── manage.py
    ├── media                                   媒体类文件目录
    ├── requirements.txt
    ├── static                                  静态文件目录
    └── templates                               模板文件目录
```

## 三、CICD
```
dev:开发环境分支
uat:测试环境分支
master:生产环境分支

发布流程:
假如当前版本是1.0.0，即将发布一个新版本1.0.1。

1、开发人员在deb分支上开发，开发完1.0.1的功能后上传各自代码。
2、由项目负责人确认大家都提交了最新代码，提交MR，将dev分支合并到uat分支。
3、代码review，确认没问题处理MR，合并分支。
4、打tag，基于uat分支打tag，自动触发CICD，将1.0.1版本功能自动部署到测试环境。
5、测试人员测试。
6、有bug，重复1、2、3步骤，删除老tag，重新打1.0.1tag，触发CICD。
7、bug修复，测试也没问题。提交MR，将uat分支合并到master分支。
8、代码review，确认没问题处理MR，合并分支。
9、打tag，基于master分支打tag，自动触发CICD，此时需要手工介入，启动Job。
```


**git规范**
* 一个功能一个commit，多个commit可以在一次push中。  
* commit格式：  
  类型[模块]内容，例如：fix[user]修复用户模块导入问题。
```
类型：
feat：新功能（feature）
perf：优化（perfact）
fix：修补bug
docs：文档（documentation）
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试
chore：构建过程或辅助工具的变动```
1111