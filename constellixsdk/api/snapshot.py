from constellixsdk.util import parse_payload


class DomainSnapshot():
    """
    Domain Snapshot object
    """

    def __init__(self, apiclient, domainid, payload):
        self.__api_client = apiclient
        self.__domain_id = domainid

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__version             = parse_payload(payload, "version")
        self.__updatedAt           = parse_payload(payload, "updatedAt")

        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def version(self):
        try:
            return self.__version
        except AttributeError:
            return None

    @property
    def updatedAt(self):
        try:
            return self.__updatedAt
        except AttributeError:
            return None
