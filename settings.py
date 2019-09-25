from os import environ
try:
    from .local_settings import Config as LConfig
    class Config(LConfig):
        pass
except:
    class Config(object):

        DEBUG = False

        HOST = '0.0.0.0'
        PORT = 8000
        WORKERS = 1
        ACCESS_LOG = True

# 微信 小程序账号信息
        WXAPP_ID = environ.get('WXAPP_ID', 'appid')
        WXAPP_SECRET = environ.get('WXAPP_SECRET', 'secret')
        WXAPP_TOKEN = environ.get('WXAPP_TOKEN', 'token')
        WXAPP_ENCODINGAESKEY = environ.get('WXAPP_ENCODINGAESKEY', '')
