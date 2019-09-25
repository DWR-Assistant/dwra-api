# -*- coding:utf-8 -*-

import logging
from app import app
from settings import Config as config

#print('db host: %s' % settings.mysql.host)

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT, workers=config.WORKERS, access_log=config.ACCESS_LOG)
