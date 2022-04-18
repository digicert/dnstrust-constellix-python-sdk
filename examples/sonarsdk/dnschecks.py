from sonarsdk import SonarApi, SonarApiError
from sonarsdk import DNSCheckParam

sonar = SonarApi("api_key", "secret_key")

# This call will return all available DNS Checks.
try:
    checks = sonar.DNSChecks.all()
    print("DNS Checks:")
    for c in checks:
        print("id {}; name {}".format(c.id, c.name))
except SonarApiError as err:
    print(err.message)

# Create DNS Check
param = DNSCheckParam()
param.name = "Sample DNS Check"
param.fqdn = "google.co.uk"
param.port = 53
param.resolver = "8.8.8.8"
param.scheduleInterval = "NONE"
param.resolverIPVersion = "IPV4"
param.recordType = "A"
param.queryProtocol = "UDP"
param.compareOptions = "ANYMATCH"
param.dnssec = False
param.userId = 300000000
param.interval = "THIRTYSECONDS"
param.monitorIntervalPolicy = "PARALLEL"
param.checkSites = [1]
param.scheduleId = 0
param.notificationReportTimeout = 1440
param.verificationPolicy = "SIMPLE"

try:
    id = sonar.DNSChecks.create_dns_check(param)
except SonarApiError as err:
    print(err.message)

# Get DNS Check by id
try:
    check = sonar.DNSChecks.get_dns_check(id=111)
except SonarApiError as err:
    print(err.message)

# Update DNS Check
param = DNSCheckParam()
param.name = "Sample DNS Check Again"
param.checkSites = [1, 2]

try:
    check = check.update(param)
except SonarApiError as err:
    print(err.message)

# Delete DNS Check
try:
    check.delete()
except SonarApiError as err:
    print(err.message)

# Run DNS Check on all agents
try:
    results = check.run_check(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run DNS Check on selected agents
try:
    results = check.run_check(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Run DNS Check Trace on all agents
try:
    results = check.check_trace(agentIds=None)
except SonarApiError as err:
    print(err.message)

# Run DNS Check Trace on selected agents
try:
    results = check.check_trace(agentIds=[111, 222])
except SonarApiError as err:
    print(err.message)

# Start DNS Check action
try:
    check.start()
except SonarApiError as err:
    print(err.message)

# Stop DNS Check action
try:
    check.stop()
except SonarApiError as err:
    print(err.message)

# DNS Check State action
try:
    state = check.check_state()
except SonarApiError as err:
    print(err.message)

# DNS Check Status action
try:
    status = check.check_status()
except SonarApiError as err:
    print(err.message)

# Http Check Agents Status
try:
    agentsStatus = check.check_agents_status()
except SonarApiError as err:
    print(err.message)
