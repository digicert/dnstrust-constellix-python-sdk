from constellixsdk.util import parse_payload, param_to_json


class IpFilter():
    """
    IPFilter object
    """
    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__rulesLimit          = parse_payload(payload, "rulesLimit")
        self.__continents          = parse_payload(payload, "continents")
        self.__countries           = parse_payload(payload, "countries")
        self.__asn                 = parse_payload(payload, "asn")
        self.__ipv4                = parse_payload(payload, "ipv4")
        self.__ipv6                = parse_payload(payload, "ipv6")
        self.__regions             = parse_payload(payload, "regions")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current IpFilter object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("ipfilters/{}".format(self.__id))

    def update(self, param):
        """
        Updates the IpFilter object.
        param is IPFilterParam containing new IpFilter fields
        Returns Updated IPFilter object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "ipfilters/{}".format(self.__id),
            body=payload
        )
        return IpFilter(self.__api_client, result["data"])

    @property
    def id(self):
        """
        The ID for this IP filter
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name for this IP filter
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def rulesLimit(self):
        """
        Upper limit is the quota assigned to the account.
        """
        try:
            return self.__rulesLimit
        except AttributeError:
            return None

    @property
    def continents(self):
        """
        A list of continents in this filter
        """
        try:
            return self.__continents
        except AttributeError:
            return None

    @property
    def countries(self):
        """
        2 digit ISO code for countries in this filter
        """
        try:
            return self.__countries
        except AttributeError:
            return None

    @property
    def asn(self):
        """
        AS Numbers that this rule applies to.
        """
        try:
            return self.__asn
        except AttributeError:
            return None

    @property
    def ipv4(self):
        """
        IPv4 addresses and CIDRs that this filter applies to
        """
        try:
            return self.__ipv4
        except AttributeError:
            return None

    @property
    def ipv6(self):
        """
        IPv6 addresses and CIDRs that this filter applies to
        """
        try:
            return self.__ipv6
        except AttributeError:
            return None

    @property
    def regions(self):
        """
        Regions or Regions and ASNs this filter applies to
        """
        try:
            return self.__regions
        except AttributeError:
            return None