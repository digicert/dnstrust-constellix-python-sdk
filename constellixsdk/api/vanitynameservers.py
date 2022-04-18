import math
from constellixsdk.api.vanitynameserver import VanityNameserver
from constellixsdk.util import CheckEmpty, param_to_json


class VanityNameserverParam():
    """
    Param for Create and Update operations
    """

    class NameserverGroup(CheckEmpty):
        def __init__(self):

            # integer : The ID of the nameserver group
            self.id = None

            # string : The name of the nameserver group
            self.name = ""
            pass

    def __init__(self):

        # string : A unique name for this vanity nameserver
        self.name = ""

        # boolean : Is this the default nameserver for domains in the account
        self.default = None

        # nameserver group
        self.nameserverGroup = VanityNameserverParam.NameserverGroup()

        # array of strings <hostname> : The nameserver hostnames
        self.nameservers = []
        pass


class VanityNameservers():
    """
    Managing VanityNameservers endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all VanityNameservers in the account
        """
        vanitynameservers = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("vanitynameservers")
            else:
                payload = self.__api_client.do_get(
                    "vanitynameservers",
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                vanitynameservers.append(
                    VanityNameserver(self.__api_client, data)
                )
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

        return vanitynameservers

    def after(self, cursor):
        """
        Cursor pagination for VanityNameserver objects
        """
        vanitynameservers = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("vanitynameservers")
        else:
            payload = self.__api_client.do_get(
                "vanitynameservers",
                params={"page": currentPage}
            )

        for data in payload["data"]:
            vanitynameservers.append(VanityNameserver(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return vanitynameservers, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return vanitynameservers, cursor

    def get_vanity_nameserver(self, id):
        """
        Fetches a single VanityNameserver in your account
        """
        result = self.__api_client.do_get("vanitynameservers/{}".format(id))
        return VanityNameserver(self.__api_client, result["data"])

    def create_vanity_nameserver(self, param):
        """
        Creates a new VanityNameserver in your account.
        param is VanityNameserverParam containing new VanityNameserver fields
        Returns the id of created VanityNameserver
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post("vanitynameservers", body=payload)
        return result["data"]["id"]
