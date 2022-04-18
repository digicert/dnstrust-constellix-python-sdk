from sonarsdk import SonarApi, SonarApiError
from sonarsdk import HTTPCheckParam

sonar = SonarApi("api_key", "secret_key")

# This call will return all available HTTP Checks.
try:
    checks = sonar.HTTPChecks.all()
    print("HTTP Checks:")
    for c in checks:
        print("id {}; name {}".format(c.id, c.name))
except SonarApiError as err:
    print(err.message)

# Create HTTP Check
param = HTTPCheckParam()
param.name = "Sample HTTP Check"
param.host = "constellix.com"
param.ipVersion = "IPV4"
param.port = 80
param.protocolType = "HTTPS"
param.checkSites = [
    1,
    2
]

try:
    id = sonar.HTTPChecks.create_http_check(param)
except SonarApiError as err:
    print(err.message)

# Get HTTP Check by id
try:
    check = sonar.HTTPChecks.get_http_check(id=111)
except SonarApiError as err:
    print(err.message)

# Update HTTP Check
param = HTTPCheckParam()
param.name = "Sample HTTP Check Again"
param.port = 443
param.protocolType = "HTTPS"
param.checkSites = [
    1,
    2,
    3
]

try:
    check = check.update(param)
except SonarApiError as err:
    print(err.message)

# Delete HTTP Check
try:
    check.delete()
except SonarApiError as err:
    print(err.message)

# Run HTTP Check on all agents
try:
    results = check.run_check(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run HTTP Check on selected agents
try:
    results = check.run_check(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Run HTTP Check Trace on all agents
try:
    results = check.check_trace(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run HTTP Check Trace on selected agents
try:
    results = check.check_trace(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Start HTTP Check action
try:
    check.start()
except SonarApiError as err:
    print(err.message)

# Stop HTTP Check action
try:
    check.stop()
except SonarApiError as err:
    print(err.message)

# HTTP Check State action
try:
    state = check.check_state()
except SonarApiError as err:
    print(err.message)

# HTTP Check Status action
try:
    status = check.check_status()
except SonarApiError as err:
    print(err.message)

# Http Check Agents Status
try:
    agentsStatus = check.check_agents_status()
except SonarApiError as err:
    print(err.message)
