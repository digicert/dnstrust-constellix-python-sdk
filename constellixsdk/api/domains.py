import math
from constellixsdk.api.domain import Domain
from constellixsdk.util import CheckEmpty, param_to_json


class SoaParam(CheckEmpty):
    """
    The SOA details for the domain
    """
    def __init__(self):
        # string : Primary master nameserver for the domain
        self.primaryNameserver = ""

        # string : Email of the administrator for the domain.
        # @ should be replaced with .
        self.email = ""

        # integer : The Time To Live (TTL) in seconds for the SOA record
        self.ttl = None

        # integer : The interval for secondary nameservers
        # should query for the SOA record
        self.refresh = None

        # integer : The number of seconds after which secondary servers
        # should retry to request the serial number
        # if the master does not respond
        self.retry = None

        # integer : Number of seconds after which secondary nameservers
        # should stop responding to queries, if the master does not respond
        self.expire = None

        # integer : How long NXDOMAIN responses should be cached for
        self.negativeCache = None
        pass


class DomainParam():
    """
    Domain Param for create and update operations
    """
    def __init__(self):
        # string : The name of the domain
        self.name = ""

        # object : The SOA details for the domain
        self.soa = SoaParam()

        # string : A note for the domain
        self.note = ""

        # boolean : Is GeoIP functionality enabled for the domain
        self.geoip = None

        # boolean : Is Global Traffic Director enabled for the domain
        self.gtd = None

        # integer : The template to use for creating this domain.
        # It will be linked to this template so any changes
        # made to the template will apply to this domain.
        self.template = None

        # list of integers : Contactlists to be notified
        # if the domain is updated
        self.contacts = []

        # integer : The vanity nameserver to use for this domain.
        self.vanity_nameserver = None

        # list of integers : The numeric IDs of tags
        # you want to apply to this domain
        self.tags = []
        pass


class Domains():
    """
    Managing Domains endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all domains in the account
        """
        domains = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("domains")
            else:
                payload = self.__api_client.do_get(
                    "domains", params={"page": currentPage}
                )
            for data in payload["data"]:
                domains.append(Domain(self.__api_client, data))
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

        return domains

    def after(self, cursor):
        """
        Cursor pagination for Domains objects
        """
        domains = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("domains")
        else:
            payload = self.__api_client.do_get(
                "domains", params={"page": currentPage}
            )

        for data in payload["data"]:
            domains.append(Domain(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return domains, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return domains, cursor

    def get_domain(self, id):
        """
        Fetches a single domain in your account
        """
        payload = self.__api_client.do_get("domains/{}".format(id))
        return Domain(self.__api_client, payload["data"])

    def create_domain(self, param):
        """
        Creates a new domain in your account.
        param is DomainParam contains Domain fields
        Returnes created Domain id
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post("domains", body=payload)
        return result["data"]["id"]
