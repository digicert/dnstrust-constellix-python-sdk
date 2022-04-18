from constellixsdk.api.domain import Domain
from constellixsdk.api.template import Template
from constellixsdk.util import parse_payload, param_to_json


class PoolItoConfig():
    """
    Pool Ito Config object
    """
    def __init__(self, payload):
        self.__period = parse_payload(payload, "period")
        self.__maximumNumberOfResults = parse_payload(
            payload, "maximumNumberOfResults"
        )
        self.__deviationAllowance = parse_payload(
            payload, "deviationAllowance"
        )
        self.__monitoringRegion = parse_payload(payload, "monitoringRegion")
        self.__handicapFactor = parse_payload(payload, "handicapFactor")

    @property
    def period(self):
        """
        The number of seconds between each check
        """
        try:
            return self.__period
        except AttributeError:
            return None

    @property
    def maximumNumberOfResults(self):
        """
        The maximum number of results to return
        """
        try:
            return self.__maximumNumberOfResults
        except AttributeError:
            return None

    @property
    def deviationAllowance(self):
        """
        Percentage of how much is the response time allowed to deviate?
        """
        try:
            return self.__deviationAllowance
        except AttributeError:
            return None

    @property
    def monitoringRegion(self):
        """
        Where monitoring should be performed from
        """
        try:
            return self.__monitoringRegion
        except AttributeError:
            return None

    @property
    def handicapFactor(self):
        """
        Enum: "none" "percent" "speed"
        """
        try:
            return self.__handicapFactor
        except AttributeError:
            return None


class PoolIto():
    """
    Pool Ito object
    """

    def __init__(self, payload):
        self.__enabled = parse_payload(payload, "enabled")
        self.__config  = PoolItoConfig(parse_payload(payload, "config"))

    @property
    def enabled(self):
        """
        Is Ito enabled for this pool?
        """
        try:
            return self.__enabled
        except AttributeError:
            return None

    @property
    def config(self):
        """
        The Ito configuration
        """
        try:
            return self.__config
        except AttributeError:
            return None


class PoolValue():
    """
    Pool Value onject
    """

    def __init__(self, payload):
        self.__value        = parse_payload(payload, "value")
        self.__weight       = parse_payload(payload, "weight")
        self.__enabled      = parse_payload(payload, "enabled")
        self.__handicap     = parse_payload(payload, "handicap")
        self.__policy       = parse_payload(payload, "policy")
        self.__sonarCheckId = parse_payload(payload, "sonarCheckId")

    @property
    def value(self):
        """
        <ipv4> or <ipv6> or <hostname>
        """
        try:
            return self.__value
        except AttributeError:
            return None

    @property
    def weight(self):
        """
        A weight for the value. Must be between 1 and 1000000
        """
        try:
            return self.__weight
        except AttributeError:
            return None

    @property
    def enabled(self):
        """
        Is this value enabled or not?
        """
        try:
            return self.__enabled
        except AttributeError:
            return None

    @property
    def handicap(self):
        """
        A handicap for this value
        """
        try:
            return self.__handicap
        except AttributeError:
            return None

    @property
    def policy(self):
        """
        The failover/check policy for this value
        """
        try:
            return self.__policy
        except AttributeError:
            return None

    @property
    def sonarCheckId(self):
        """
        The ID of the check to use from Sonar
        """
        try:
            return self.__sonarCheckId
        except AttributeError:
            return None


class Pool():
    """
    Pool object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__type                = parse_payload(payload, "type")
        self.__name                = parse_payload(payload, "name")
        self.__return              = parse_payload(payload, "return")
        self.__minimumFailover     = parse_payload(payload, "minimumFailover")
        self.__failed              = parse_payload(payload, "failed")
        self.__enabled             = parse_payload(payload, "enabled")

        self.__domains = []
        domains = parse_payload(payload, "domains")
        if domains:
            for d in domains:
                self.__domains.append(Domain(self.__api_client, d))

        self.__templates = []
        templates = parse_payload(payload, "templates")
        if templates:
            for t in templates:
                self.__templates.append(Template(self.__api_client, t))

        self.__contacts = []
        contacts = parse_payload(payload, "contacts")
        if contacts:
            for c in contacts:
                self.__contacts.append(c["id"])

        self.__ito                 = PoolIto(parse_payload(payload, "ito"))
        self.__values = []
        values = parse_payload(payload, "values")
        if values:
            for v in values:
                self.__values.append(PoolValue(v))

        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current Pool object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete(
            "pools/{}/{}".format(self.__type, self.__id)
        )

    def update(self, param):
        """
        Updates the Pool object.
        param is PoolParam containing new Pool fields
        Returns updated Pool object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "pools/{}/{}".format(self.__type, self.__id),
            body=payload
        )
        return Pool(self.__api_client, result["data"])

    @property
    def id(self):
        """
        The ID of the Pool object
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def typeValue(self):
        """
        The type of pool
        """
        try:
            return self.__type
        except AttributeError:
            return None

    @property
    def name(self):
        """
        A name for the pool
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def returnValue(self):
        """
        The minimum number of entries from the pool to return when queried
        """
        try:
            return self.__return
        except AttributeError:
            return None

    @property
    def minimumFailover(self):
        """
        The number of records that must be available
        for this pool to be used for failover
        """
        try:
            return self.__minimumFailover
        except AttributeError:
            return None

    @property
    def failed(self):
        """

        """
        try:
            return self.__failed
        except AttributeError:
            return None

    @property
    def enabled(self):
        """
        Whether the pool is enabled or not
        """
        try:
            return self.__enabled
        except AttributeError:
            return None

    @property
    def domains(self):
        """
        Domain objects associated to the pool
        """
        try:
            return self.__domains
        except AttributeError:
            return None

    @property
    def templates(self):
        """
        Template objects associated to the pool
        """
        try:
            return self.__templates
        except AttributeError:
            return None

    @property
    def contacts(self):
        """
        Contact lists to be emailed when this pool changes
        """
        try:
            return self.__contacts
        except AttributeError:
            return None

    @property
    def ito(self):
        """
        PoolIto object
        """
        try:
            return self.__ito
        except AttributeError:
            return None

    @property
    def values(self):
        """
        Pool values
        """
        try:
            return self.__values
        except AttributeError:
            return None
