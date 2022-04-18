from sonarsdk import SonarApi, SonarApiError
from sonarsdk.api.enums import *
from sonarsdk import DNSCheckParam

sonar = SonarApi()

print("QA DNS Checks operations")
# get all DNS checks

checks = sonar.DNSChecks.all()
initialLen = len(checks)

for c in checks:
    print("DNS Check id={}; name={}".format(c.id, c.name))
    if c.name in ["QA Test DNS Check", "QA Test DNS Check Update"]:
        c.delete()

checks = sonar.DNSChecks.all()
initialLen = len(checks)

# Create DNS check
print("Create DNS check")
param = DNSCheckParam()
param.name = "QA Test DNS Check"
param.fqdn = "google.co.uk"
param.port = 53
param.resolver = "8.8.8.8"
param.scheduleInterval = ScheduleInterval.NONE
param.resolverIPVersion = IPVersion.IPV4
param.recordType = RecordType.A
param.queryProtocol = ProtocolType.UDP
param.compareOptions = CompareOption.ANYMATCH
param.dnssec = False
param.userId = 300000000
param.interval = MonitorInterval.THIRTYSECONDS
param.monitorIntervalPolicy = MonitorIntervalPolicy.PARALLEL
param.checkSites = [1]
param.scheduleId = 0
param.notificationReportTimeout = 1440
param.verificationPolicy = VerificationPolicy.SIMPLE
param.runTraceroute = RunTraceroute.DISABLED

id = sonar.DNSChecks.create_dns_check(param)
print("Check type id={} is".format(id), sonar.CheckType(id))

checks = sonar.DNSChecks.all()
if initialLen + 1 != len(checks):
    raise Exception("DNS Check create operation error")

new_check = sonar.DNSChecks.get_dns_check(id)
print("New DNS Check id={}; name={}".format(new_check.id, new_check.name))

# Update operation
print("Update DNS check")
param = DNSCheckParam()
param.name = "QA Test DNS Check Update"
param.runTraceroute = RunTraceroute.DISABLED
param.checkSites = [1, 2]

new_check = new_check.update(param)

if new_check.name != "QA Test DNS Check Update":
    raise Exception("DNS Check update operation error")

# get single DNS Check operation
new_check = sonar.DNSChecks.get_dns_check(new_check.id)
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

# Delete DNS Check operation
new_check.delete()

checks = sonar.DNSChecks.all()
if initialLen  != len(checks):
    raise Exception("DNS Check delete operation error")
