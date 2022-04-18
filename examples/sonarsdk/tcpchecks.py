from sonarsdk import SonarApi, SonarApiError
from sonarsdk import TCPCheckParam

sonar = SonarApi("api_key", "secret_key")

# This call will return all available TCP Checks.
try:
    checks = sonar.TCPChecks.all()
    print("TCP Checks:")
    for c in checks:
        print("id {}; name {}".format(c.id, c.name))
except SonarApiError as err:
    print(err.message)

# Create TCP Check
param = TCPCheckParam()
param.name = "Sample TCP Check"
param.host = "constellix.com"
param.ipVersion = "IPV4"
param.port = 80
param.checkSites = [1, 2]

try:
    id = sonar.TCPChecks.create_tcp_check(param)
except SonarApiError as err:
    print(err.message)

# Get TCP Check by id
try:
    check = sonar.TCPChecks.get_tcp_check(id=111)
except SonarApiError as err:
    print(err.message)

# Update TCP Check
param = TCPCheckParam()
param.name = "Sample TCP Check Again"
param.port = 443
param.checkSites = [1, 2, 3]

try:
    check = check.update(param)
except SonarApiError as err:
    print(err.message)

# Delete TCP Check
try:
    check.delete()
except SonarApiError as err:
    print(err.message)

# Run TCP Check on all agents
try:
    results = check.run_check(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run TCP Check on selected agents
try:
    results = check.run_check(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Run TCP Check Trace on all agents
try:
    results = check.check_trace(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run TCP Check Trace on selected agents
try:
    results = check.check_trace(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Start TCP Check action
try:
    check.start()
except SonarApiError as err:
    print(err.message)

# Stop TCP Check action
try:
    check.stop()
except SonarApiError as err:
    print(err.message)

# TCP Check State action
try:
    state = check.check_state()
except SonarApiError as err:
    print(err.message)

# TCP Check Status action
try:
    status = check.check_status()
except SonarApiError as err:
    print(err.message)

# Http Check Agents Status
try:
    agentsStatus = check.check_agents_status()
except SonarApiError as err:
    print(err.message)
