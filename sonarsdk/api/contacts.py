from sonarsdk.util import parse_payload


class ContactAddress():
    """
    Sonar Contact Address object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__address     = parse_payload(payload, "address")
        self.__active      = parse_payload(payload, "active")
        self.__contactId   = parse_payload(payload, "contactId")
        self.__type        = parse_payload(payload, "type")

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return None

    @property
    def active(self):
        try:
            return self.__active
        except AttributeError:
            return None

    @property
    def contactId(self):
        try:
            return self.__contactId
        except AttributeError:
            return None

    @property
    def typeValue(self):
        try:
            return self.__type
        except AttributeError:
            return None


class Contact():
    """
    Sonar Contact object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id             = parse_payload(payload, "id")
        self.__firstName      = parse_payload(payload, "firstName")
        self.__lastName       = parse_payload(payload, "lastName")
        self.__accountId      = parse_payload(payload, "accountId")
        self.__addresses = []
        addresses_payload = parse_payload(payload, "addresses")
        for addr in addresses_payload:
            self.__addresses.append(ContactAddress(apiclient, addr))

    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def firstName(self):
        try:
            return self.__firstName
        except AttributeError:
            return None

    @property
    def lastName(self):
        try:
            return self.__lastName
        except AttributeError:
            return None

    @property
    def accountId(self):
        try:
            return self.__accountId
        except AttributeError:
            return None

    @property
    def addresses(self):
        try:
            return self.__addresses
        except AttributeError:
            return None


class Group():
    """
    Sonar Contact Group object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id     = parse_payload(payload, "id")
        self.__name   = parse_payload(payload, "name")

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


class Contacts():
    """
    Managing Sonar Contacts endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def allContacts(self):
        """
        Returns a list of all contacts configured within the account
        """
        contacts = []
        payload = self.__api_client.do_get("contacts")

        for data in payload:
            contacts.append(Contact(self.__api_client, data))

        return contacts

    def allGroups(self):
        """
        Returns a list of all contact groups within the account
        """
        groups = []
        payload = self.__api_client.do_get("contact/groups")

        for data in payload:
            groups.append(Group(self.__api_client, data))

        return groups
