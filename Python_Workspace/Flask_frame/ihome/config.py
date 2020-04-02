import redis


class Config:

    SECRET_KEY = "weigbsHDGI25./+sdg5"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    # redis地址
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session的配置
    SESSION_TYPE = "redis"        # session数据保存在redis中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True     # 对cookie中session_id进行加密处理，依赖于SECRET_KEY
    PERMANENT_SESSION_LIFETIME = 86400   # session数据的有效期，单位秒


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境的配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}