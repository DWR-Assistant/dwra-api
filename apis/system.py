import sys
from app import app
from sanic.log import logger
from sanic.response import json
from models.oauth import Account

@app.route('/version', methods=['GET'])
async def version_get(request):
    sys.path.append("..")
    path = 'version'
    with open(path) as f:
        a = f.read()
        a = a.strip('\n')
    logger.info(a)
    return json({"version": a})

@app.route('/test', methods=['GET'])
async def test_get(request):
    print(Account())
    return json(str(Account()))

@app.route('/test1', methods=['GET'])
async def test1_get(request):
    print(Account.objects)
    return json(str(Account()))
