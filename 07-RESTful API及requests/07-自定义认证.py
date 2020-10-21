from requests.auth import AuthBase
import requests


class MyAuth(AuthBase):
    """Attaches HTTP my custom Authentication to the given Request object."""

    def __init__(self, token):
        # setup any auth-related data here
        self.token = token

    def __call__(self, r):
        # modify and return the request
        r.headers['custom-token'] = self.token
        return r


if __name__ == '__main__':
    response = requests.get('http://pizzabin.org/admin', auth=MyAuth('XXXXXX'))
    print(response)
