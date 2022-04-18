import os

from constellixsdk.client import ApiClient
from constellixsdk.api.domains import Domains
from constellixsdk.api.templates import Templates
from constellixsdk.api.pools import Pools
from constellixsdk.api.ipfilters import IpFilters
from constellixsdk.api.geoproximities import GeoProximities
from constellixsdk.api.vanitynameservers import VanityNameservers
from constellixsdk.api.contactlists import ContactLists
from constellixsdk.api.tags import Tags
from constellixsdk.api.announcements import Announcements


class ConstellixApi():
    """
    Entry point to Constellix API
    """

    def __init__(self, apikey=None, secret=None):
        if not apikey:
            apikey = os.environ.get("CONSTELLIX_API_KEY")
        if not secret:
            secret = os.environ.get("CONSTELLIX_SECRET_KEY")

        self.__api_client = ApiClient(apikey, secret)

        self.__Domains = Domains(self.__api_client)
        self.__Templates = Templates(self.__api_client)
        self.__Pools = Pools(self.__api_client)
        self.__IpFilters = IpFilters(self.__api_client)
        self.__GeoProximities = GeoProximities(self.__api_client)
        self.__VanityNameservers = VanityNameservers(self.__api_client)
        self.__ContactLists = ContactLists(self.__api_client)
        self.__Tags = Tags(self.__api_client)
        self.__Announcements = Announcements(self.__api_client)

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
    def Domains(self):
        """
        Domains endpoint wrapper
        """
        return self.__Domains

    @property
    def Templates(self):
        """
        Templates endpoint wrapper
        """
        return self.__Templates

    @property
    def Pools(self):
        """
        Pools endpoint wrapper
        """
        return self.__Pools

    @property
    def IpFilters(self):
        """
        IpFilters endpoint wrapper
        """
        return self.__IpFilters

    @property
    def GeoProximities(self):
        """
        GeoProximities endpoint wrapper
        """
        return self.__GeoProximities

    @property
    def VanityNameservers(self):
        """
        VanityNameservers endpoint wrapper
        """
        return self.__VanityNameservers

    @property
    def ContactLists(self):
        """
        ContactLists endpoint wrapper
        """
        return self.__ContactLists

    @property
    def Tags(self):
        """
        Tags endpoint wrapper
        """
        return self.__Tags

    @property
    def Announcements(self):
        """
        Announcements endpoint wrapper
        """
        return self.__Announcements
