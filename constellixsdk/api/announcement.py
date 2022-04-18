from constellixsdk.util import parse_payload


class Announcement():
    """
    Announcement object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id              = parse_payload(payload, "id")
        self.__type            = parse_payload(payload, "type")
        self.__link            = parse_payload(payload, "link")
        self.__title           = parse_payload(payload, "title")

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
    def typeValue(self):
        try:
            return self.__type
        except AttributeError:
            return None

    @property
    def link(self):
        try:
            return self.__link
        except AttributeError:
            return None

    @property
    def title(self):
        try:
            return self.__title
        except AttributeError:
            return None
