from sonarsdk import SonarApi, SonarApiError
from sonarsdk.api.enums import *
from sonarsdk import HTTPCheckParam

sonar = SonarApi()

print("QA HTTP Checks operations")
# get all HTTP checks

checks = sonar.HTTPChecks.all()
initialLen = len(checks)

for c in checks:
    print("HTTP Check id={}; name={}".format(c.id, c.name))
    if c.name in ["QA Test HTTP Check", "QA Test HTTP Check Update"]:
        c.delete()

checks = sonar.HTTPChecks.all()
initialLen = len(checks)

# Create HTTP check
print("Create HTTP check")
param = HTTPCheckParam()
param.name = "QA Test HTTP Check"
param.host = "constellix.com"
param.ipVersion = IPVersion.IPV4
param.port = 80
param.protocolType = ProtocolType.HTTPS
param.checkSites = [
    1,
    2
]

try:
    id = sonar.HTTPChecks.create_http_check(param)
except SonarApiError as err:
    print("URL {}".format(sonar.last_request_url))
    print("Body {}".format(sonar.last_request_body))
    print("Response Status code {}".format(sonar.last_response.status_code))
    print("Response Text {}".format(sonar.last_response.text))
    raise err

checks = sonar.HTTPChecks.all()
if initialLen + 1 != len(checks):
    raise Exception("HTTP Check create operation error")

new_check = sonar.HTTPChecks.get_http_check(id)
print("New HTTP Check id={}; name={}".format(new_check.id, new_check.name))

# Update operation
print("Update HTTP check")
param = HTTPCheckParam()
param.name = "QA Test HTTP Check Update"
param.port = 80
param.protocolType = ProtocolType.HTTPS
param.checkSites = [
    1,
    2
]

new_check = new_check.update(param)

if new_check.name != "QA Test HTTP Check Update":
    raise Exception("HTTP Check update operation error")

# get single HTTP Check operation
new_check = sonar.HTTPChecks.get_http_check(new_check.id)
print(new_check.name)

# Run Check operation
results = new_check.run_check()
print("Check results for all agents")
for r in results:
    print(r.status)

results = new_check.run_check([1, 2])
print("Check results for two agents")
for r in results:
    print(r.status)

# Run Trace operation
results = new_check.check_trace()
print("Trace results for all agents")
for r in results:
    print(r.result)

results = new_check.check_trace([1, 2])
print("Trace results for two agents")
for r in results:
    print(r.result)

# Check Agent Status
print("Check Agent Status")
new_check.check_agents_status()

# Start
print("Check Start")
new_check.start()

# Stop
print("Check Stop")
new_check.stop()

# Check State
print("Check State")
print(new_check.check_state())

# Check Status
print("Check Status")
try:
    print(new_check.check_status())
except SonarApiError as err:
    print(sonar.last_request_url)
    print(sonar.last_request_body)
    print(err.message)
    raise err

# Delete HTTP Check operation
new_check.delete()

checks = sonar.HTTPChecks.all()
if initialLen  != len(checks):
    raise Exception("HTTP Check delete operation error")
