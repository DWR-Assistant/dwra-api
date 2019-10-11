
def get_wxapp_userinfo(encrypted_data, iv, code):
    from weixin.lib.wxcrypt import WXBizDataCrypt
    from weixin import WXAPPAPI
    from weixin.oauth2 import OAuth2AuthExchangeError
    appid = Config.WXAPP_ID
    secret = Config.WXAPP_SECRET
    api = WXAPPAPI(appid=appid, app_secret=secret)
    try:
        # 使用 code  换取 session key
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        raise Unauthorized(e.code, e.description)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(appid, session_key)
    # 解密得到 用户信息
    user_info = crypt.decrypt(encrypted_data, iv)
    return user_info


def verify_wxapp(encrypted_data, iv, code):
    user_info = get_wxapp_userinfo(encrypted_data, iv, code)
    # 获取 openid
    openid = user_info.get('openId', None)
    if openid:
        auth = Account.get_by_wxapp(openid)
        if not auth:
            raise Unauthorized('wxapp_not_registered')
        return auth
    raise Unauthorized('invalid_wxapp_code')


def create_token(request):
    # verify basic token
    approach = request.json.get('auth_approach')
    username = request.json['username']
    password = request.json['password']
    if approach == 'password':
        account = verify_password(username, password)
    elif approach == 'wxapp':
        account = verify_wxapp(username, password, request.args.get('code'))
    if not account:
        return False, {}
    payload = {
        "iss": Config.ISS,
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": Config.AUDIENCE,
        "sub": str(account['_id']),
        "nickname": account['nickname'],
        "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    # 由于 account 中 _id 是一个 object 需要转化成字符串
    return True, {'access_token': token, 'account_id': str(account['_id'])}
