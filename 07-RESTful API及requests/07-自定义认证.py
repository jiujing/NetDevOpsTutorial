from requests.auth import AuthBase
import requests


class ZetMircoServiceAuth(AuthBase):
    """Attaches HTTP my custom Authentication to the given Request object."""

    def __init__(self,app_token=None,jwt_token=None):
        # 参数个数和名称我们可以按需设置，可多个（0-N）
        if jwt:
            self.token =token
        else:
           s .t =  settings.token

    def __call__(self, r):
        # 进行自定义认证的过程，r代表的是request请求，我们可以修改它的heaers等等信息。
        r.headers['zet-token'] = self.token
        return r


if __name__ == '__main__':
    response = requests.get('http://pizzabin.org/admin', auth=ZetMircoServiceAuth(jwt_token=request.header['x-api']))
    print(response)
