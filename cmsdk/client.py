from auth import OAuthHeader
import requests


class CmClient(object):
    BASE_URI = "https://api.cardmarket.com/ws/v2.0/output.json/"
    ACCOUNT = "account"
    ORDERS = "orders"
    STOCK = "stock"

    def __init__(self, app_token, app_secret, access_token, access_secret):
        self.__oauth = OAuthHeader(app_token, app_secret, access_token, access_secret)

    def get_account(self):
        return self.__http_get(self.ACCOUNT)

    def get_stock(self, start=None):
        path = self.STOCK
        if start is not None:
            path = path + '/' + str(start)
        return self.__http_get(path)

    def get_orders(self, actor, state, start=None):
        path = '{}/{}/{}'.format(self.ORDERS, actor, state)
        if start is not None:
            path += '/' + str(start)
        return self.__http_get(path)

    def __http_get(self, path, params=None):
        endpoint = self.BASE_URI + path
        headers = {"Content-Type": "application/json", "Authorization": self.__oauth.get_auth_header("GET",endpoint, params)}
        rs = requests.get(endpoint, params=params, headers=headers, allow_redirects=False)

        return rs.json()
