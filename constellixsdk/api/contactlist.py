from constellixsdk.util import parse_payload, param_to_json


class ContactEmail():
    """
    Contact Email object
    """

    def __init__(self, payload):
        self.__address  = parse_payload(payload, "address")
        self.__verified = parse_payload(payload, "verified")

    @property
    def address(self):
        """
        Contact Email address
        """
        try:
            return self.__address
        except AttributeError:
            return None

    @property
    def verified(self):
        """
        Is Contact Email verified or not
        """
        try:
            return self.__verified
        except AttributeError:
            return None


class ContactList():
    """
    ContactList object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id            = parse_payload(payload, "id")
        self.__name          = parse_payload(payload, "name")
        self.__emailCount    = parse_payload(payload, "emailCount")
        self.__emails = []
        emails = parse_payload(payload, "emails")
        if emails:
            for e in emails:
                self.__emails.append(ContactEmail(e))

        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current ContactList object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("contactlists/{}".format(self.__id))

    def update(self, param):
        """
        Updates the ContactList object.
        param is ContactListParam containing new ContactList fields
        Returns updated ContactList object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "contactlists/{}".format(self.__id),
            body=payload
        )
        return ContactList(self.__api_client, result["data"])

    @property
    def id(self):
        """
        ID for this contact list
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        A name for this contact list
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def emailCount(self):
        try:
            return self.__emailCount
        except AttributeError:
            return None

    @property
    def emails(self):
        """
        List of ContactEmails objects
        """
        try:
            return self.__emails
        except AttributeError:
            return None
