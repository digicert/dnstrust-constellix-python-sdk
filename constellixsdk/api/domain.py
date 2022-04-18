from constellixsdk.util import parse_payload, param_to_json
from constellixsdk.api.soa import Soa
from constellixsdk.api.domainrecords import DomainRecords
from constellixsdk.api.domainhistory import DomainHistory
from constellixsdk.api.domainsnapshots import DomainSnapshots


class Domain():
    """
    Domain object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__status              = parse_payload(payload, "status")
        self.__soa                 = Soa(parse_payload(payload, "soa"))
        self.__geoip               = parse_payload(payload, "geoip")
        self.__gtd                 = parse_payload(payload, "gtd")
        self.__nameservers         = parse_payload(payload, "nameservers")

        self.__tags = []
        tags = parse_payload(payload, "tags")
        if tags:
            for t in tags:
                self.__tags.append(t["id"])

        try:
            self.__template         = parse_payload(payload, "template")["id"]
        except:
            self.__template = None

        try:
            self.__vanityNameserver = parse_payload(
                payload,
                "vanityNameserver"
            )["id"]
        except:
            self.__vanityNameserver = None

        self.__contacts = []
        contacts = parse_payload(payload, "contacts")
        if contacts:
            for c in contacts:
                self.__contacts.append(c["id"])

        self.__note                = parse_payload(payload, "note")

        self.__records = DomainRecords(self.__api_client, self.__id)
        self.__history = DomainHistory(self.__api_client, self.__id)
        self.__snaphots = DomainSnapshots(self.__api_client, self.__id)
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def DomainRecords(self):
        """
        Managing domain records
        """
        return self.__records

    @property
    def DomainHistory(self):
        """
        Managing domain history
        """
        return self.__history

    @property
    def DomainSnapshots(self):
        """
        Managing domain snaphots
        """
        return self.__snaphots

    def delete(self):
        """
        Delete current domain object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("domains/{}".format(self.__id))

    def update(self, param):
        """
        Updates the domain object.
        param is DomainParam containing new Domain fields
        Returns Updated Domain object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "domains/{}".format(self.__id),
            body=payload
        )
        return Domain(self.__api_client, result["data"])

    def get_nameservers(self):
        """
        Fetches the current nameservers the domain is using.
        This may be different from the ones assigned to it by Constellix.
        Returns a list of nameservers
        """
        if not self.__id:
            return None

        data = self.__api_client.do_get(
            "domains/{}/nameservers".format(self.__id)
        )
        return data["data"]["nameservers"]

    @property
    def id(self):
        """
        ID of Domain object
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name of the domain
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def status(self):
        """
        Status of the domain
        """
        try:
            return self.__status
        except AttributeError:
            return None

    @property
    def soa(self):
        """
        The SOA details for the domain
        """
        try:
            return self.__soa
        except AttributeError:
            return None

    @property
    def geoip(self):
        """
        Is GeoIP functionality enabled for the domain
        """
        try:
            return self.__geoip
        except AttributeError:
            return None

    @property
    def gdt(self):
        """
        Is Global Traffic Director enabled for the domain
        """
        try:
            return self.__gtd
        except AttributeError:
            return None

    @property
    def nameservers(self):
        """
        List of nameservers for the domain
        """
        try:
            return self.__nameservers
        except AttributeError:
            return None

    @property
    def tags(self):
        """
        list
        The numeric IDs of tags
        """
        try:
            return self.__tags
        except AttributeError:
            return None

    @property
    def template(self):
        """
        The template ID to use for creating this domain
        """
        try:
            return self.__template
        except AttributeError:
            return None

    @property
    def vanityNameserver(self):
        """
        The vanity nameserver ID to use for this domain.
        """
        try:
            return self.__vanityNameserver
        except AttributeError:
            return None

    @property
    def contacts(self):
        """
        list
        Contactlists IDs to be notified if the domain is updated
        """
        try:
            return self.__contacts
        except AttributeError:
            return None

    @property
    def note(self):
        """
        A note for the domain
        """
        try:
            return self.__note
        except AttributeError:
            return None
