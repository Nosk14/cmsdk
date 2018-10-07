from time import time
from urllib.parse import quote
from hashlib import sha1
import hmac
import uuid
import base64


def to_bytearray(string):
    return bytearray(string, 'ascii')

def percent_encode(string):
    return quote(string, safe='')


class OAuthHeader:
    def __init__(self, app_token, app_secret, access_token, access_secret):
        self.__app_token = app_token
        self.__app_secret = app_secret
        self.__access_token = access_token
        self.__access_secret = access_secret

    def get_auth_header(self, method, endpoint, http_params):
        params = {}
        if http_params is not None:
            params = http_params

        headers = {
            "oauth_consumer_key": self.__app_token,
            "oauth_token": self.__access_token,
            "oauth_nonce": str(uuid.uuid4()),
            "oauth_timestamp": str(int(time())),
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_version": "1.0",
        }

        signature = self.__generate_signature(method, endpoint, params, headers)
        headers.update({"realm": percent_encode(endpoint), "oauth_signature": signature})

        return "OAuth " + ",".join('{}="{}"'.format(k,v) for k,v in headers.items())

    def __get_base_string(self, method, endpoint, oauth_values):
        string_values = "&".join(["{}={}".format(percent_encode(k), percent_encode(v)) for k,v in oauth_values.items()])
        quoted_endpoint = percent_encode(endpoint)

        return "&".join([method.upper(), quoted_endpoint, percent_encode(string_values)])

    def __generate_signature(self, method, endpoint, http_params, headers):
        oauth_values = {**headers, **http_params}
        sorted_keys = sorted(oauth_values)
        sorted_oauth_values = dict([(k,oauth_values[k]) for k in sorted_keys ])

        base_string = self.__get_base_string(method, endpoint, sorted_oauth_values)

        signing_key = "&".join([percent_encode(self.__app_secret), percent_encode(self.__access_secret)])

        hashed = hmac.new(to_bytearray(signing_key), to_bytearray(base_string), sha1)

        signature = base64.b64encode((hashed.digest()))

        return signature.decode('ascii')


