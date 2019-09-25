import sys
from app import app
from sanic.log import logger
from sanic.response import json

@app.route('/version', methods=['GET'])
async def version_get(request):
    sys.path.append("..")
    path = 'version'
    with open(path) as f:
        a = f.read()
        a = a.strip('\n')
    logger.info(a)
    return json({"version": a})
