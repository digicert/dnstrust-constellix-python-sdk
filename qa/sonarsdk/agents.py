from sonarsdk import SonarApi, SonarApiError
from sonarsdk.api.enums import *
from sonarsdk import HTTPTestParam
from sonarsdk import TraceTestParam
from sonarsdk import TCPTestParam
from sonarsdk import DNSTestParam

sonar = SonarApi()

try:
    agents = sonar.Agents.all_agents()
    print("Agents:")
    for a in agents:
        print("id {}; name {}; label {}".format(a.id, a.name, a.label))
except SonarApiError as err:
    print(err.message)
    raise(err)

agent = agents[0]

# Sample HTTP Test on agent
param = HTTPTestParam()
param.host = "www.google.com"
param.port = 443
param.expectedStatusCode = 200
param.ipVersion = IPVersion.IPV4

try:
    testResult = agent.http_test(param)
    print("Test Result:")
    print(testResult.payload)
except SonarApiError as err:
    print("\nError details:")
    print("Error Message: " + err.message)
    print("Request Body: " + sonar.last_request_body)
    print("Request URL: " + sonar.last_request_url)
    print("Response status code: " + str(sonar.last_response.status_code))
    print("Response text: " + sonar.last_response.text)

# Sample Trace Test on agent
param = TraceTestParam()
param.host = "www.google.com"
param.ipVersion = IPVersion.IPV4
param.type = ProtocolType.UDP

try:
    testResult = agent.trace_test(param)
    print("Test Result:")
    print(testResult.payload)
except SonarApiError as err:
    print("\nError details:")
    print("Error Message: " + err.message)
    print("Request Body: " + sonar.last_request_body)
    print("Request URL: " + sonar.last_request_url)
    print("Response status code: " + str(sonar.last_response.status_code))
    print("Response text: " + sonar.last_response.text)


# Sample TCP Test on agent
param = TCPTestParam()
param.host = "www.google.com"
param.port = 80
param.ipVersion = IPVersion.IPV4

try:
    testResult = agent.tcp_test(param)
    print("Test Result:")
    print(testResult.payload)
except SonarApiError as err:
    print("\nError details:")
    print("Error Message: " + err.message)
    print("Request Body: " + sonar.last_request_body)
    print("Request URL: " + sonar.last_request_url)
    print("Response status code: " + str(sonar.last_response.status_code))
    print("Response text: " + sonar.last_response.text)


# Sample DNS Test on agent
param = DNSTestParam()
param.host = "www.google.com"
param.nameServer = "ns2.google.com"
param.recordType = RecordType.A

try:
    testResult = agent.dns_test(param)
    print("Test Result:")
    print(testResult.payload)
except SonarApiError as err:
    print("\nError details:")
    print("Error Message: " + err.message)
    print("Request Body: " + sonar.last_request_body)
    print("Request URL: " + sonar.last_request_url)
    print("Response status code: " + str(sonar.last_response.status_code))
    print("Response text: " + sonar.last_response.text)
