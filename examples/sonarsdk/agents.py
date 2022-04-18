from sonarsdk import SonarApi, SonarApiError
from sonarsdk import DNSTestParam
from sonarsdk import HTTPTestParam
from sonarsdk import TraceTestParam
from sonarsdk import TCPTestParam

sonar = SonarApi("api_key", "secret_key")

# This call will return all available agents.
try:
    agents = sonar.Agents.all_agents()
    print("Agents:")
    for a in agents:
        print("id {}; name {}; label {}".format(a.id, a.name, a.label))
except SonarApiError as err:
    print(err.message)

agent = agents[0]

# Sample HTTP Test on agent
param = HTTPTestParam()
param.host = "www.google.com"
param.port = 443
param.expectedStatusCode = 200
param.ipVersion = "IPV4"

try:
    testResult = agent.http_test(param)
except SonarApiError as err:
    print(err.message)

# Sample Trace Test on agent
param = TraceTestParam()
param.host = "www.google.com"
param.ipVersion = "IPV4"
param.type = "UDP"

try:
    testResult = agent.trace_test(param)
except SonarApiError as err:
    print(err.message)

# Sample TCP Test on agent
param = TCPTestParam()
param.host = "www.google.com"
param.port = 80
param.ipVersion = "IPV4"

try:
    testResult = agent.tcp_test(param)
except SonarApiError as err:
    print(err.message)

# Sample DNS Test on agent
param = DNSTestParam()
param.host = "www.google.com"
param.nameServer = "ns2.google.com"
param.recordType = "A"

try:
    testResult = agent.dns_test(param)
except SonarApiError as err:
    print(err.message)
