文件结构说明:
 ihome  项目主目录
    ├── config.py  项目配置文件，分为生产环境和开发环境
    ├── ihome  核心开发逻辑存放目录
    │   ├── api_1_0  蓝图目录
    │   │   ├── demo.py  蓝图装饰的视图函数文件
    │   │   └── __init__.py   创建蓝图对象
    │   ├── __init__.py   初始化app对象、db对象、redis链接、csrf防护、Session类对象、注册蓝图
    │   ├── libs   用于存放项目中用到一些库文件 依赖文件
    │   ├── models.py  模型类文件
    │   ├── static   静态资源
    │   └── utilis   实用工具
    ├── logs  日志文件
    │   └── log
    ├── manager.py   管理整个项目的启动，以及数据库迁移
    └── readme.txt
