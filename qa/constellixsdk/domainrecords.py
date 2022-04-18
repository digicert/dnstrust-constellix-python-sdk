from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import DomainParam
from constellixsdk import RecordParam

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
print("New Domain id={}; name={}".format(
    new_domain.id, new_domain.name
))

records = new_domain.DomainRecords.all()
recordsTotal = len(records)

print("Creating Domain Record")

param = RecordParam()
param.type = RecordParam.Type.A
param.name = "www"
param.value = []
value = RecordParam.RecordValue()
value.enabled = True
value.value = "198.51.100.42"
param.value.append(value)

record_id = new_domain.DomainRecords.create_domain_record(param)
print("New record id = {}".format(record_id))

try:
    record = new_domain.DomainRecords.get_domain_record(record_id)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("New Record id={}; name={}; type={}".format(
    record.id, record.name, record.typeValue
))
print("New Record contacts={};".format(record.contactsId))

print("Updating Domain Record")
param = RecordParam()
param.value = []

value1 = RecordParam.RecordValue()
value1.enabled = True
value1.value = "198.51.100.42"
param.value.append(value1)

value2 = RecordParam.RecordValue()
value2.enabled = True
value2.value = "198.51.100.41"
param.value.append(value2)

try:
    u_record = record.update(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Deleting Domain Record")
record.delete()

records = new_domain.DomainRecords.all()
if recordsTotal != len(records):
    raise Exception("Error deleting record")

# delete domain
print("Deleting domain")
new_domain.delete()
