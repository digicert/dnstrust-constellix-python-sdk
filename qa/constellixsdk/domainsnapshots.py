from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import DomainParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all domain
print("Domains:")
domains = constellix.Domains.all()
for d in domains:
    print("Domain id={}; name={}".format(d.id, d.name))
    if d.name == "cnsxtestdomain.com":
        d.delete()

# create domain
print("Creating Domain")
try:
    param = DomainParam()
    param.name = "cnsxtestdomain.com"
    param.soa.primaryNameserver = "ns11.constellix.com"
    param.soa.email = "admin.example.com"
    param.soa.ttl = 86400
    param.soa.refresh = 86400
    param.soa.retry = 7200
    param.soa.expire = 3600000
    param.soa.negativeCache = 180
    param.note = "Test Domain"
    param.geoip = True
    param.gtd = True

    id = constellix.Domains.create_domain(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Domain created with id={}".format(id))

new_domain = constellix.Domains.get_domain(id)
print("New Domain id={}; name={}".format(new_domain.id, new_domain.name))

# Get Snapshots
print("Domain Snapshots")
try:
    snapshots = new_domain.DomainSnapshots.all()
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

for s in snapshots:
    print("Snapshot id={}; name={}; version={}".format(
        s.id, s.name, s.version
    ))

print("Get Snapshot")
if len(snapshots) > 0:
    snapshot = new_domain.DomainHistory.get_history_version(snapshots[0].version)
    print("Snapshot id={}; name={}; version={}".format(
        snapshot.id, snapshot.name, snapshot.version
    ))

print("Apply Snapshot")
# new_domain.DomainHistory.apply_history(3)

print("Delete Snapshot")
# new_domain.DomainHistory.snapshot_history(3)

# delete domain
print("Deleting domain")
new_domain.delete()
