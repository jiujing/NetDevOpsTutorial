import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    response = requests.get('http://pizzabin.org/admin', auth=HTTPBasicAuth(username='admin',password='password'))
    print(response)
