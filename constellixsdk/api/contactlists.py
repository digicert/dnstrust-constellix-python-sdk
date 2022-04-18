import math
from constellixsdk.api.contactlist import ContactList
from constellixsdk.util import param_to_json


class ContactListParam():
    """
    Contact List Param for Create and Update operations
    """
    def __init__(self):

        # string : A name for this contact list
        self.name = ""

        # list of strings : The emails in this list
        self.emails = []
        pass


class ContactLists():
    """
    Managing ContactLists endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all ContactLists in the account
        """
        contactlists = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("contactlists")
            else:
                payload = self.__api_client.do_get(
                    "contactlists",
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                contactlists.append(ContactList(self.__api_client, data))
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

        return contactlists

    def after(self, cursor):
        """
        Cursor pagination for ContactList objects
        """
        contactlists = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("contactlists")
        else:
            payload = self.__api_client.do_get(
                "contactlists", params={"page": currentPage}
            )

        for data in payload["data"]:
            contactlists.append(ContactList(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return contactlists, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return contactlists, cursor

    def get_contact_list(self, id):
        """
        Fetches a single ContactList in your account
        """
        result = self.__api_client.do_get("contactlists/{}".format(id))
        return ContactList(self.__api_client, result["data"])

    def create_contact_list(self, param):
        """
        Creates a new ContactList in your account.
        param is ContactListParam containing new ContactList fields:
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post("contactlists", body=payload)
        return result["data"]["id"]
