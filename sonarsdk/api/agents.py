from sonarsdk.sonarapierror import SonarApiError
from sonarsdk.util import parse_payload, param_to_json
from sonarsdk.api.testresult import TestResult, TraceTestResult


class HTTPTestParam():
    """
    Param for HTTP Test
    """
    def __init__(self):
        self.host = ""
        self.port = None
        self.protocolType = ""
        self.path = ""
        self.fqdn = ""
        self.stringToSearch = ""
        self.expectedStatusCode = None
        self.ipVersion = ""
        pass


class TCPTestParam():
    """
    Param for TCP Test
    """
    def __init__(self):
        self.host = ""
        self.port = None
        self.stringToSearch = ""
        self.ipVersion = ""
        self.stringToSend = ""
        self.stringToReceive = ""
        pass


class DNSTestParam():
    """
    Param for DNS Test
    """
    def __init__(self):
        self.host = ""
        self.nameServer = ""
        self.recordType = ""
        self.expectedIp = ""
        pass


class TraceTestParam():
    """
    Param for Trace Test
    """
    def __init__(self):
        self.host = ""
        self.ipVersion = ""
        self.type = ""
        pass


class Agent():
    """
    Sonar System Agent object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id           = parse_payload(payload, "id")
        self.__name         = parse_payload(payload, "name")
        self.__label        = parse_payload(payload, "label")
        self.__location     = parse_payload(payload, "location")
        self.__country      = parse_payload(payload, "country")
        self.__region       = parse_payload(payload, "region")

    def http_test(self, param):
        """
        Run an instant HTTP test
        param is HTTPTestParam
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "test/http/{}".format(self.__id), body=payload
        )
        print(result)
        try:
            return TestResult(self.__api_client, result[0])
        except Exception:
            raise SonarApiError(message = "Unexpected Result") from None

    def trace_test(self, param):
        """
        Run an instant Trace test
        param is TraceTestParam
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "test/trace/{}".format(self.__id), body=payload
        )
        try:
            return TraceTestResult(self.__api_client, result[0])
        except Exception:
            raise SonarApiError(message = "Unexpected Result") from None

    def tcp_test(self, param):
        """
        Run an instant TCP test
        param is TCPTestParam
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "test/tcp/{}".format(self.__id), body=payload
        )
        try:
            return TestResult(self.__api_client, result[0])
        except Exception:
            raise SonarApiError(message = "Unexpected Result") from None

    def dns_test(self, param):
        """
        Run an instant DNS test
        param is DNSTestParam
        """
        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "test/dns/{}".format(self.__id), body=payload
        )
        try:
            return TestResult(self.__api_client, result[0])
        except Exception:
            raise SonarApiError(message = "Unexpected Result") from None

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
    def label(self):
        try:
            return self.__label
        except AttributeError:
            return None

    @property
    def location(self):
        try:
            return self.__location
        except AttributeError:
            return None

    @property
    def country(self):
        try:
            return self.__country
        except AttributeError:
            return None

    @property
    def region(self):
        try:
            return self.__region
        except AttributeError:
            return None


class Agents():
    """
    Managing System Agents endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all_agents(self):
        """
        Returns a list of all available agents
        """
        agents = []
        payload = self.__api_client.do_get("system/sites")

        for data in payload:
            agents.append(Agent(self.__api_client, data))

        return agents
