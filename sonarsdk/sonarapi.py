import os

from sonarsdk.sonarapiclient import SonarApiClient
from sonarsdk.api.contacts import Contacts
from sonarsdk.api.agents import Agents
from sonarsdk.api.httpchecks import HTTPChecks
from sonarsdk.api.tcpchecks import TCPChecks
from sonarsdk.api.dnschecks import DNSChecks


class SonarApi():
    """
    Entry point to Sonar API
    """

    def __init__(self, apikey=None, secret=None):
        if not apikey:
            apikey = os.environ.get("CONSTELLIX_API_KEY")
        if not secret:
            secret = os.environ.get("CONSTELLIX_SECRET_KEY")

        self.__api_client = SonarApiClient(apikey, secret)

        self.__Contacts = Contacts(self.__api_client)
        self.__Agents = Agents(self.__api_client)
        self.__HTTPChecks = HTTPChecks(self.__api_client)
        self.__TCPChecks = TCPChecks(self.__api_client)
        self.__DNSChecks = DNSChecks(self.__api_client)

    @property
    def last_request_url(self):
        return self.__api_client.last_request_url

    @property
    def last_request_body(self):
        return self.__api_client.last_request_body

    @property
    def last_response(self):
        return self.__api_client.last_response

    @property
    def Contacts(self):
        """
        Sonar Contacts endpoint wrapper
        """
        return self.__Contacts

    @property
    def Agents(self):
        """
        Sonar Agents endpoint wrapper
        """
        return self.__Agents

    @property
    def HTTPChecks(self):
        """
        Sonar HTTP Checks operations wrapper
        """
        return self.__HTTPChecks

    @property
    def TCPChecks(self):
        """
        Sonar TCP Checks operations wrapper
        """
        return self.__TCPChecks

    @property
    def DNSChecks(self):
        """
        Sonar DNS Checks operations wrapper
        """
        return self.__DNSChecks

    def CheckType(self, id):
        """
        Get Check type by ID
        """
        payload = self.__api_client.do_get("check/type/{}".format(id))
        return payload["type"]
