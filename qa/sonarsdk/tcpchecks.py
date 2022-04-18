from sonarsdk import SonarApi, SonarApiError
from sonarsdk.api.enums import *
from sonarsdk import TCPCheckParam

sonar = SonarApi()

print("QA TCP Checks operations")
# get all TCP checks

checks = sonar.TCPChecks.all()
initialLen = len(checks)

for c in checks:
    print("TCP Check id={}; name={}".format(c.id, c.name))
    if c.name in ["QA Test TCP Check", "QA Test TCP Check Update"]:
        c.delete()

checks = sonar.TCPChecks.all()
initialLen = len(checks)

# Create TCP check
print("Create TCP check")
param = TCPCheckParam()
param.name = "QA Test TCP Check"
param.host = "constellix.com"
param.ipVersion = IPVersion.IPV4
param.port = 80
param.checkSites = [1, 2]

id = sonar.TCPChecks.create_tcp_check(param)

checks = sonar.TCPChecks.all()
if initialLen + 1 != len(checks):
    raise Exception("TCP Check create operation error")

new_check = sonar.TCPChecks.get_tcp_check(id)
print("New TCP Check id={}; name={}".format(new_check.id, new_check.name))

# Update operation
print("Update TCP check")
param = TCPCheckParam()
param.name = "QA Test TCP Check Update"
param.port = 80
param.checkSites = [1]

try:
    new_check = new_check.update(param)
except SonarApiError as err:
    print(sonar.last_request_url)
    print(sonar.last_request_body)
    print(err.message)
    raise err
print("Second Update TCP check")

try:
    new_check = new_check.update(param)
except SonarApiError as err:
    print(sonar.last_request_url)
    print(sonar.last_request_body)
    print(err.message)
    raise err

if new_check.name != "QA Test TCP Check Update":
    raise Exception("TCP Check update operation error")

# get single TCP Check operation
new_check = sonar.TCPChecks.get_tcp_check(new_check.id)
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
    print(err.response.status_code)
    print(err.response.text)
    raise err

# Delete TCP Check operation
new_check.delete()

checks = sonar.TCPChecks.all()
if initialLen  != len(checks):
    raise Exception("TCP Check delete operation error")
