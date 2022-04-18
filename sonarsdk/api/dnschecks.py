from sonarsdk.util import parse_payload, join_url_array_params
from sonarsdk.util import parse_uri_id, param_to_json
from sonarsdk.api.testresult import TestResult, TraceTestResult


class DNSCheckParam():
    """
    Param for DNSCheck Create and Update operations
    """
    def __init__(self):
        self.name = ""
        self.fqdn = ""
        self.port = None
        self.resolver = ""
        self.expectedResponse = []
        self.note = ""
        self.scheduleInterval = ""
        self.resolverIPVersion = ""
        self.recordType = ""
        self.queryProtocol = ""
        self.compareOptions = ""
        self.dnssec = None
        self.userId = None
        self.interval = ""
        self.monitorIntervalPolicy = ""
        self.checkSites = []
        self.notificationGroups = []
        self.scheduleId = None
        self.notificationReportTimeout = None
        self.verificationPolicy = ""
        self.runTraceroute = ""
        pass


class DNSCheck():
    """
    Sonar DNS Check object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id               = parse_payload(payload, "id")
        self.__name             = parse_payload(payload, "name")
        self.__fqdn             = parse_payload(payload, "fqdn")
        self.__resolver         = parse_payload(payload, "resolver")
        self.__note             = parse_payload(payload, "note")
        self.__scheduleInterval = parse_payload(
            payload, "scheduleInterval"
        )
        self.__userId                    = parse_payload(payload, "userId")
        self.__monitorIntervalPolicy     = parse_payload(
            payload, "monitorIntervalPolicy"
        )
        self.__interval                  = parse_payload(payload, "interval")
        self.__notificationGroups        = parse_payload(
            payload, "notificationGroups"
        )
        self.__checkSites                = parse_payload(payload, "checkSites")
        self.__notificationReportTimeout = parse_payload(
            payload, "notificationReportTimeout"
        )
        self.__scheduleId = parse_payload(payload, "scheduleId")
        self.__verificationPolicy = parse_payload(
            payload, "verificationPolicy"
        )
        self.__runTraceroute = parse_payload(payload, "runTraceroute")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current Check object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("dns/{}".format(self.__id))

    def update(self, param):
        """
        Update a dns check in Sonar
        param is DNSCheckParam
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "dns/{}".format(self.__id), body=payload
        )
        return DNSCheck(self.__api_client, result)

    def run_check(self, agentIds = None):
        """
        This call will run the specified check
        from the agent defined in the params.
        If no agent is defined, the check will be run
        from all selected agents for that check
        agentIds is a list of agents to run check on
        """
        if not self.__id:
            return None

        siteids = join_url_array_params("siteIds", agentIds)
        result = self.__api_client.do_get(
            "dns/{}/test{}".format(self.__id, siteids)
        )
        results = []
        for r in result:
            results.append(TestResult(self.__api_client, r))
        return results

    def check_trace(self, agentIds = None):
        """
        This will run a trace on an existing Check
        from the defined agent.
        If no agent is defined the a trace will be run
        from every agent defined within the check
        agentIds is a list of agents to run check on
        """
        if not self.__id:
            return None

        siteids = join_url_array_params("siteIds", agentIds)
        result = self.__api_client.do_get(
            "dns/{}/trace{}".format(self.__id, siteids)
        )
        results = []
        for r in result:
            results.append(TraceTestResult(self.__api_client, r))
        return results

    def start(self):
        """
        This call will start the defined DNS check
        """
        if not self.__id:
            return None

        self.__api_client.do_put("dns/{}/start".format(self.__id))

    def stop(self):
        """
        This call will stop the defined DNS check
        """
        if not self.__id:
            return None

        self.__api_client.do_put("dns/{}/stop".format(self.__id))

    def check_status(self):
        """
        This call will return the current status of the check
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get("dns/{}/status".format(self.__id))
        return result["status"]

    def check_agents_status(self):
        """
        This call will return the check status
        from all sites selected for that check
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get(
            "dns/{}/site/status".format(self.__id)
        )
        return result

    def check_state(self):
        """
        This call will return weather the check is active or inactive
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get("dns/{}/state".format(self.__id))
        return result["state"]

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
    def fqdn(self):
        try:
            return self.__fqdn
        except AttributeError:
            return None

    @property
    def resolver(self):
        try:
            return self.__resolver
        except AttributeError:
            return None

    @property
    def note(self):
        try:
            return self.__note
        except AttributeError:
            return None

    @property
    def scheduleInterval(self):
        try:
            return self.__scheduleInterval
        except AttributeError:
            return None

    @property
    def userId(self):
        try:
            return self.__userId
        except AttributeError:
            return None

    @property
    def interval(self):
        try:
            return self.__interval
        except AttributeError:
            return None

    @property
    def monitorIntervalPolicy(self):
        try:
            return self.__monitorIntervalPolicy
        except AttributeError:
            return None

    @property
    def checkSites(self):
        try:
            return self.__checkSites
        except AttributeError:
            return None

    @property
    def notificationGroups(self):
        try:
            return self.__notificationGroups
        except AttributeError:
            return None

    @property
    def scheduleId(self):
        try:
            return self.__scheduleId
        except AttributeError:
            return None

    @property
    def notificationReportTimeout(self):
        try:
            return self.__notificationReportTimeout
        except AttributeError:
            return None

    @property
    def verificationPolicy(self):
        try:
            return self.__verificationPolicy
        except AttributeError:
            return None

    @property
    def runTraceroute(self):
        try:
            return self.__runTraceroute
        except AttributeError:
            return None


class DNSChecks():
    """
    Managing Sonar DNS Checks operations
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all configured DNS checks within your Sonar account
        """
        checks = []

        payload = self.__api_client.do_get("dns")
        for data in payload:
            checks.append(DNSCheck(self.__api_client, data))

        return checks

    def get_dns_check(self, id):
        """
        Fetches a single DNS check in your account
        """
        payload = self.__api_client.do_get("dns/{}".format(id))
        return DNSCheck(self.__api_client, payload)

    def create_dns_check(self, param):
        """
        Creates a new DNS check in your account.
        param is DNSCheckParam
        """
        payload = param_to_json(param)

        self.__api_client.do_post("dns", body=payload)
        id = parse_uri_id(self.__api_client.last_response.headers["Location"])
        return id
