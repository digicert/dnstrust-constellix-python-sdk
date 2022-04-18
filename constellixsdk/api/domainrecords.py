import math
from constellixsdk.api.domainrecord import DomainRecord
from enum import Enum
from constellixsdk.util import CheckEmpty, param_to_json


class RecordParam():
    """
    Record param for DomainRecord and TemplateRecord
    Create and Update operations
    """

    class RecordValueExtended(CheckEmpty):
        """
        Record Value
        """
        def __init__(self):
            # boolean : Whether the failover entry is enabled or not.
            # Disabled entries will not be included in a response
            self.enabled = None

            # integer : The sort order of the entry.
            # Lower order entries are preferred over higher order entries
            self.order = None

            # integer : The ID in Sonar to use for checking
            # if the record should be used
            self.sonarCheckId = None

            # string : <ipv4>
            self.value = ""
            pass

    class RecordValue(CheckEmpty):
        """
        Record Value
        """
        def __init__(self):
            # boolean : Whether the failover entry is enabled or not.
            # Disabled entries will not be included in a response
            self.enabled = None

            # string : <ipv4>
            self.value = ""
            pass

    class RecordValueMode(CheckEmpty):
        """
        Record value
        """

        class Mode(Enum):
            NORMAL = "normal"
            OFF = "off"
            ONE_WAY = "one-way"

        def __init__(self):
            # string : The failover mode
            self.mode = ""

            # list of RecordValueExtended : list of values
            self.values = []
            pass

    class Type(Enum):
        """
        The type of record values
        """
        A = "A"
        AAAA = "AAAA"
        ANAME = "ANAME"
        CAA = "CAA"
        CERT = "CERT"
        CNAME = "CNAME"
        HINFO = "HINFO"
        HTTP = "HTTP"
        MX = "MX"
        NAPTR = "NAPTR"
        NS = "NS"
        PTR = "PTR"
        RP = "RP"
        SPF = "SPF"
        SRV = "SRV"
        TXT = "TXT"

    class Region(Enum):
        DEFAULT = "default"
        EUROPE = "europe"
        US_EAST = "us-east"
        US_WEST = "us-west"
        ASIA_PACIFIC = "asia-pacific"
        OCEANIA = "oceania"
        SOUTH_AMERICA = "south-america"

    class Mode(Enum):
        STANDARD = "standard"
        FAILOVER = "failover"
        ROUNDROBIN_FAILOVER = "roundrobin-failover"
        POOLS = "pools"

    def __init__(self):
        # string : The type of record to add
        self.type = ""

        # string : The name for the record
        self.name = ""

        # boolean : Whether the record is enabled
        self.enabled = None

        # integeer : How long DNS servers should cache the record for
        self.ttl = None

        # string : A description of the record.
        # It must be 512 characters or less.
        self.notes = ""

        # string : Optional region for this record. Will default to 'default'
        self.region = ""

        # integer : The integer ID of an IP Filter to use for this record.
        # Cannot be used with GeoPeoximity.
        self.ipfilter = None

        # integer : The integer ID of a GeoProximity to use for this record.
        # Cannot be used with IP Filter.
        self.geoproximity = None

        # string : The current mode for this.
        # For most records this is just 'standard' which is the default.
        # A, ANAME, AAAA and CNAME, can have other options.
        self.mode = ""

        # list of integers : Contact lists to be notified
        # if a failover happens in a failover mode.
        self.contacts = []

        # required
        # list of RecordValue objects, or
        # RecordValueMode, or
        # list of RecordValueExtended, or
        # list of integers (Numeric ID of the pool)
        self.value = None
        pass


class DomainRecords():
    """
    Managing DomainRecords endpoint wrapper
    """

    def __init__(self, apiclient, domainid):
        self.__api_client = apiclient
        self.__domain_id = domainid

    def all(self):
        """
        Returns a list of all DomainRecords in the Domain
        """
        domainrecords = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get(
                    "domains/{}/records".format(self.__domain_id)
                )
            else:
                payload = self.__api_client.do_get(
                    "domains/{}/records".format(self.__domain_id),
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                domainrecords.append(
                    DomainRecord(self.__api_client, self.__domain_id, data)
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

        return domainrecords

    def after(self, cursor):
        """
        Cursor pagination for DomainRecord objects
        """
        domainrecords = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get(
                "domains/{}/records".format(self.__domain_id)
            )
        else:
            payload = self.__api_client.do_get(
                "domains/{}/records".format(self.__domain_id),
                params={"page": currentPage}
            )

        for data in payload["data"]:
            domainrecords.append(
                DomainRecord(self.__api_client, self.__domain_id, data)
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
            return domainrecords, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return domainrecords, cursor

    def get_domain_record(self, id):
        """
        Fetches a single DomainRecord in Domain
        """
        result = self.__api_client.do_get(
            "domains/{}/records/{}".format(self.__domain_id, id)
        )
        return DomainRecord(
            self.__api_client,
            self.__domain_id,
            result["data"]
        )

    def create_domain_record(self, param):
        """
        Creates a new DomainRecord in Domain
        param is RecordParam containing new DomainRecord fields
        Returns the ID of created DomainRecord object
        """

        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "domains/{}/records".format(self.__domain_id),
            body=payload
        )
        return result["data"]["id"]
