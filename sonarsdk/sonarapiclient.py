import requests
import json
import base64
import hashlib
import hmac
import sys
from time import time

from sonarsdk.sonarapierror import SonarApiError
from sonarsdk.sonarapierror import NotAuthorized
from sonarsdk.sonarapierror import RequestCouldNotBeProcessed
from sonarsdk import util


class SonarApiClient():
    """
    Api Client
    """

    def __init__(self, apikey, secret):
        self.__baseurl = "https://api.sonar.constellix.com/rest/api"
        self.__apikey = apikey
        self.__secret = secret
        self.__last_response = None
        self.__last_request_url = ""
        self.__last_request_body = ""

    @property
    def last_request_url(self):
        return self.__last_request_url

    @property
    def last_request_body(self):
        return self.__last_request_body

    @property
    def last_response(self):
        return self.__last_response

    def do_get(self, url, params=None, body=None):
        url = util.join_url(self.__baseurl, url)
        if params:
            url = util.join_url_params(url, params)
        return self.__do_request('GET', url, body)

    def do_post(self, url, params=None, body=None):
        url = util.join_url(self.__baseurl, url)
        if params:
            url = util.join_url_params(url, params)
        return self.__do_request('POST', url, body)

    def do_put(self, url, params=None, body=None):
        url = util.join_url(self.__baseurl, url)
        if params:
            url = util.join_url_params(url, params)
        return self.__do_request('PUT', url, body)

    def do_delete(self, url, params=None, body=None):
        url = util.join_url(self.__baseurl, url)
        if params:
            url = util.join_url_params(url, params)
        return self.__do_request('DELETE', url, body)

    def __do_request(self, method, url, body=None):
        self.__last_request_url = "{} {}".format(method, url)
        if body is None:
            self.__last_request_body = None
        elif isinstance(body, dict):
            self.__last_request_body = json.dumps(body)
        else:
            self.__last_request_body = body

        headers = {}
        if "dns" in url.split("/"):
            headers["Content-Type"] = "application/vnd.sonar.v2+json"
        else:
            headers["Content-Type"] = "application/json"

        epoch_ms = str(int((time()) * 1000))

        if sys.version_info[0] < 3:
            digester = hmac.new(
                str.encode(self.__secret),
                str.encode(epoch_ms), hashlib.sha1
            )
            signature = digester.digest()
            hmac_text = base64.standard_b64encode(signature)
        else:
            digester = hmac.new(
                bytes(self.__secret, "UTF-8"),
                bytes(epoch_ms, "UTF-8"),
                hashlib.sha1
            )
            signature = digester.digest()
            hmac_text = str(base64.standard_b64encode(signature), "UTF-8")

        headers["x-cns-security-token"] = "{}:{}:{}".format(
            self.__apikey, hmac_text, epoch_ms
        )

        try:
            response = requests.request(
                method, url, headers=headers, data=self.__last_request_body
            )
        except Exception as err:
            raise SonarApiError(
                message="Exception during request", exception=err
            ) from None

        self.__last_response = response

        status = response.status_code
        if status in [200, 201, 202]:
            try:
                return response.json()
            except:
                return None

        if status == 401:
            raise NotAuthorized(
                message="The request is not authorized or \
                    authorization is invalid"
            )

        if status == 404:
            raise RequestCouldNotBeProcessed(
                message="The resource requested could not be found"
            )
        try:
            error_message = "The request could not be processed. \
            Status Code = {}. Error Message: {}".format(
                status, response.text
            )
        except:
            error_message = "The request could not be processed. \
            Status Code = {}.".format(status)

        raise RequestCouldNotBeProcessed(
            message = error_message
        )
        pass
    pass
