from sonarsdk.util import parse_payload, join_url_array_params
from sonarsdk.util import parse_uri_id, param_to_json
from sonarsdk.api.testresult import TestResult, TraceTestResult


class HTTPCheckParam():
    """
    Param for HTTPCheck Create and Update operations
    """
    def __init__(self):
        self.name = ""
        self.host = ""
        self.ipVersion = ""
        self.port = None
        self.protocolType = ""
        self.checkSites = []
        self.runTraceroute = ""
        pass


class HTTPCheck():
    """
    Sonar HTTP Check object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                 = parse_payload(payload, "id")
        self.__name               = parse_payload(payload, "name")
        self.__host               = parse_payload(payload, "host")
        self.__port               = parse_payload(payload, "port")
        self.__protocolType       = parse_payload(payload, "protocolType")
        self.__ipVersion          = parse_payload(payload, "ipVersion")
        self.__fqdn               = parse_payload(payload, "fqdn")
        self.__path               = parse_payload(payload, "path")
        self.__searchString       = parse_payload(payload, "searchString")
        self.__connectionTimeout  = parse_payload(
            payload, "connectionTimeout"
        )
        self.__expectedStatusCode = parse_payload(
            payload, "expectedStatusCode"
        )
        self.__userAgent          = parse_payload(payload, "userAgent")
        self.__note               = parse_payload(payload, "note")
        self.__scheduleInterval   = parse_payload(payload, "scheduleInterval")
        self.__userId             = parse_payload(payload, "userId")
        self.__interval           = parse_payload(payload, "interval")
        self.__monitorIntervalPolicy = parse_payload(
            payload, "monitorIntervalPolicy"
        )
        self.__checkSites            = parse_payload(payload, "checkSites")
        self.__notificationGroups    = parse_payload(
            payload, "notificationGroups"
        )
        self.__scheduleId            = parse_payload(payload, "scheduleId")
        self.__notificationReportTimeout = parse_payload(
            payload, "notificationReportTimeout"
        )
        self.__verificationPolicy  = parse_payload(
            payload, "verificationPolicy"
        )
        self.__runTraceroute       = parse_payload(payload, "runTraceroute")
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

        self.__api_client.do_delete("http/{}".format(self.__id))

    def update(self, param):
        """
        Update an http check in Sonar
        param is HTTPCheckParam
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "http/{}".format(self.__id), body=payload
        )
        return HTTPCheck(self.__api_client, result)

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
            "http/{}/test{}".format(self.__id, siteids)
        )
        results = []
        for r in result:
            results.append(TestResult(self.__api_client, r))
        return results

    def check_trace(self, agentIds = None):
        """
        This will run a trace on an existing HTTP Check
        from the defined agents.
        If no agent is defined the a trace will be run
        from every agent defined within the check
        agentIds is a list of agents to run check on
        """
        if not self.__id:
            return None

        siteids = join_url_array_params("siteIds", agentIds)
        result = self.__api_client.do_get(
            "http/{}/trace{}".format(self.__id, siteids)
        )
        results = []
        for r in result:
            results.append(TraceTestResult(self.__api_client, r))
        return results

    def start(self):
        """
        This call will start the defined HTTP check
        """
        if not self.__id:
            return None

        self.__api_client.do_put("http/{}/start".format(self.__id))

    def stop(self):
        """
        This call will stop the defined HTTP check
        """
        if not self.__id:
            return None

        self.__api_client.do_put("http/{}/stop".format(self.__id))

    def check_status(self):
        """
        This call will return the current status of the check
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get("http/{}/status".format(self.__id))
        return result["status"]

    def check_agents_status(self):
        """
        This call will return the check status
        from all sites selected for that check
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get(
            "http/{}/site/status".format(self.__id)
        )
        return result

    def check_state(self):
        """
        This call will return weather the check is active or inactive
        """
        if not self.__id:
            return None

        result = self.__api_client.do_get("http/{}/state".format(self.__id))
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
    def host(self):
        try:
            return self.__host
        except AttributeError:
            return None

    @property
    def port(self):
        try:
            return self.__port
        except AttributeError:
            return None

    @property
    def protocolType(self):
        try:
            return self.__protocolType
        except AttributeError:
            return None

    @property
    def ipVersion(self):
        try:
            return self.__ipVersion
        except AttributeError:
            return None

    @property
    def fqdn(self):
        try:
            return self.__fqdn
        except AttributeError:
            return None

    @property
    def path(self):
        try:
            return self.__path
        except AttributeError:
            return None

    @property
    def searchString(self):
        try:
            return self.__searchString
        except AttributeError:
            return None

    @property
    def connectionTimeout(self):
        try:
            return self.__connectionTimeout
        except AttributeError:
            return None

    @property
    def expectedStatusCode(self):
        try:
            return self.__expectedStatusCode
        except AttributeError:
            return None

    @property
    def userAgent(self):
        try:
            return self.__userAgent
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


class HTTPChecks():
    """
    Managing Sonar HTTP Checks operations
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all configured HTTP checks within your Sonar account
        """
        checks = []

        payload = self.__api_client.do_get("http")
        for data in payload:
            checks.append(HTTPCheck(self.__api_client, data))

        return checks

    def get_http_check(self, id):
        """
        Fetches a single HTTP check in your account
        """
        payload = self.__api_client.do_get("http/{}".format(id))
        return HTTPCheck(self.__api_client, payload)

    def create_http_check(self, param):
        """
        Creates a new HTTP check in your account.
        param is HTTPCheckParam
        """
        payload = param_to_json(param)

        self.__api_client.do_post("http", body=payload)
        id = parse_uri_id(self.__api_client.last_response.headers["Location"])
        return id
