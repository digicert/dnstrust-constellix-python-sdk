from constellixsdk.util import parse_payload


class Soa():
    """
    Soa object
    """

    def __init__(self, payload):
        self.__primaryNameserver = parse_payload(payload, "primaryNameserver")
        self.__email             = parse_payload(payload, "email")
        self.__ttl               = parse_payload(payload, "ttl")
        self.__refresh           = parse_payload(payload, "refresh")
        self.__retry             = parse_payload(payload, "retry")
        self.__expire            = parse_payload(payload, "expire")
        self.__negativeCache     = parse_payload(payload, "negativeCache")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def primaryNameserver(self):
        """
        Primary master nameserver for the domain
        """
        try:
            return self.__primaryNameserver
        except AttributeError:
            return None

    @property
    def email(self):
        """
        Email of the administrator for the domain
        """
        try:
            return self.__email
        except AttributeError:
            return None

    @property
    def ttl(self):
        """
        The Time To Live (TTL) in seconds for the SOA record
        """
        try:
            return self.__ttl
        except AttributeError:
            return None

    @property
    def refresh(self):
        """
        The interval for secondary nameservers should query for the SOA record
        """
        try:
            return self.__refresh
        except AttributeError:
            return None

    @property
    def retry(self):
        """
        The number of seconds after which secondary servers should retry
        to request the serial number if the master does not respond
        """
        try:
            return self.__retry
        except AttributeError:
            return None

    @property
    def expire(self):
        """
        Number of seconds after which secondary nameservers
        should stop responding to queries,
        if the master does not respond
        """
        try:
            return self.__expire
        except AttributeError:
            return None

    @property
    def negativeCache(self):
        """
        How long NXDOMAIN responses should be cached for
        """
        try:
            return self.__negativeCache
        except AttributeError:
            return None
