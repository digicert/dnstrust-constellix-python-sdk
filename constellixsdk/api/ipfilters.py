import math
from constellixsdk.api.ipfilter import IpFilter
from constellixsdk.util import param_to_json
from enum import Enum


class IPFilterParam():
    """
    Param for IPFilter Create and Update operations
    """

    class Continents(Enum):
        WORLD = "world"
        AF = "AF"
        AN = "AN"
        AS = "AS"
        EU = "EU"
        NA = "NA"
        OC = "OC"
        SA = "SA"

    def __init__(self):
        # string : The name for this IP filter
        self.name = ""

        # integer : Values should be multiples of 100.
        # Upper limit is the quota assigned to the account.
        self.rulesLimit = None

        # array of strings : A list of continents in this filter
        self.continents = []

        # array of strings : 2 digit ISO code for countries in this filter
        # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
        self.countries = []

        # array of integers : AS Numbers that this rule applies to.
        # Values must be between 0 and 4,294,967,295
        self.asn = []

        # array of strings : IPv4 addresses and CIDRs
        # that this filter applies to
        self.ipv4 = []

        # array of strings : IPv6 addresses and CIDRs
        # that this filter applies to
        self.ipv6 = []

        self.regions = []
        pass


class IpFilters():
    """
    Managing IpFilters endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all IpFilters in the account
        """
        ipfilters = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("ipfilters")
            else:
                payload = self.__api_client.do_get(
                    "ipfilters", params={"page": currentPage}
                )
            for data in payload["data"]:
                ipfilters.append(IpFilter(self.__api_client, data))
            totalPages = 1
            try:
                totalPages = payload["meta"]["pagination"]["totalPages"]
            except:
                totalPages = math.ceil(
                    payload["meta"]["pagination"]["total"] /
                    payload["meta"]["pagination"]["perPage"]
                )
            if payload["meta"]["pagination"]["currentPage"] >= totalPages:
                break
            currentPage = payload["meta"]["pagination"]["currentPage"] + 1

        return ipfilters

    def after(self, cursor):
        """
        Cursor pagination for IPFilter objects
        """
        ipfilters = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("ipfilters")
        else:
            payload = self.__api_client.do_get(
                "ipfilters", params={"page": currentPage}
            )

        for data in payload["data"]:
            ipfilters.append(IpFilter(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return ipfilters, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return ipfilters, cursor

    def get_ip_filter(self, id):
        """
        Fetches a single IpFilter in your account
        """
        result = self.__api_client.do_get("ipfilters/{}".format(id))
        return IpFilter(self.__api_client, result["data"])

    def create_ip_filter(self, param):
        """
        Creates a new IpFilter in your account.
        param is IPFilterParam containing new IpFilter fields
        Returns the id of created IPFilter
        """
        payload = param_to_json(param)
        print(payload)

        result = self.__api_client.do_post("ipfilters", body=payload)
        return result["data"]["id"]
