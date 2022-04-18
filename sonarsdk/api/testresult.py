from sonarsdk.util import parse_payload


class MonitorAgent():
    """
    MonitorAgent object from tests result
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__agentId       = parse_payload(payload, "agentId")
        self.__siteId        = parse_payload(payload, "siteId")
        self.__status        = parse_payload(payload, "status")

    @property
    def agentId(self):
        try:
            return self.__agentId
        except AttributeError:
            return None

    @property
    def siteId(self):
        try:
            return self.__siteId
        except AttributeError:
            return None

    @property
    def status(self):
        try:
            return self.__status
        except AttributeError:
            return None


class TestResult():
    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__status            = parse_payload(payload, "status")
        self.__responseTime      = parse_payload(payload, "responseTime")
        self.__dnsLookUpTime     = parse_payload(payload, "dnsLookUpTime")
        self.__resolvedIpAddress = parse_payload(payload, "resolvedIpAddress")
        self.__statusCode        = parse_payload(payload, "statusCode")
        self.__monitorAgent      = MonitorAgent(
            self.__api_client, parse_payload(payload, "monitorAgent")
        )
        self.__message           = parse_payload(payload, "message")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def status(self):
        try:
            return self.__status
        except AttributeError:
            return None

    @property
    def responseTime(self):
        try:
            return self.__responseTime
        except AttributeError:
            return None

    @property
    def dnsLookUpTime(self):
        try:
            return self.__dnsLookUpTime
        except AttributeError:
            return None

    @property
    def resolvedIpAddress(self):
        try:
            return self.__resolvedIpAddress
        except AttributeError:
            return None

    @property
    def statusCode(self):
        try:
            return self.__statusCode
        except AttributeError:
            return None

    @property
    def monitorAgent(self):
        try:
            return self.__monitorAgent
        except AttributeError:
            return None

    @property
    def message(self):
        try:
            return self.__message
        except AttributeError:
            return None


class TraceTestResult():
    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__agent       = MonitorAgent(
            self.__api_client, parse_payload(payload, "agent")
        )
        self.__result      = parse_payload(payload, "result")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def result(self):
        try:
            return self.__result
        except AttributeError:
            return None

    @property
    def agent(self):
        try:
            return self.__agent
        except AttributeError:
            return None
