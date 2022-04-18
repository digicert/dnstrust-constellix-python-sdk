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

domains = constellix.Domains.all()
initialLen = len(domains)

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
print("New Domain id={}; name={}".format(
    new_domain.id, new_domain.name
))

domains = constellix.Domains.all()
if initialLen + 1 != len(domains):
    raise Exception("Domain Create error")

# update domain
print("Updating domain")
param = DomainParam()
param.geoip = False

try:
    updated_domain = new_domain.update(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

if updated_domain.geoip != param.geoip:
    raise Exception("Domain Update error")

# getting nameservers
print("Getting Nameservers")
try:
    nameservers = new_domain.get_nameservers()
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print(nameservers)

# delete domain
print("Deleting domain")
new_domain.delete()

domains = constellix.Domains.all()
if initialLen != len(domains):
    raise Exception("Domain Delete error")
