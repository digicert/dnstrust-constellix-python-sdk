from constellixsdk.util import parse_payload, param_to_json


class NameserverGroup():
    """
    Nameserver group object
    """

    def __init__(self, payload):
        self.__id = parse_payload(payload, "id")
        self.__name = parse_payload(payload, "name")

    @property
    def id(self):
        """
        The ID of the nameserver group
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name of the nameserver group
        """
        try:
            return self.__name
        except AttributeError:
            return None


class VanityNameserver():
    """
    VanityNameserver object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__default             = parse_payload(payload, "default")
        self.__public              = parse_payload(payload, "public")
        self.__nameserverGroup     = NameserverGroup(
            parse_payload(payload, "nameserverGroup")
        )
        self.__nameservers         = parse_payload(payload, "nameservers")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current VanityNameserver object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("vanitynameservers/{}".format(self.__id))

    def update(self, param):
        """
        Updates the VanityNameserver object.
        param is VanityNameserverParam containing new VanityNameserver fields
        Returns the updated VanityNameserver object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "vanitynameservers/{}".format(self.__id),
            body=payload
        )
        return VanityNameserver(self.__api_client, result["data"])

    @property
    def id(self):
        """
        The ID of the Vanity Nameserver
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        A unique name for this vanity nameserver
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def default(self):
        """
        Is this the default nameserver for domains in the account
        """
        try:
            return self.__default
        except AttributeError:
            return None

    @property
    def public(self):
        """
        """
        try:
            return self.__public
        except AttributeError:
            return None

    @property
    def nameserverGroup(self):
        """
        NameserverGroup object
        """
        try:
            return self.__nameserverGroup
        except AttributeError:
            return None

    @property
    def nameservers(self):
        """
        The nameserver hostnames
        """
        try:
            return self.__nameservers
        except AttributeError:
            return None
