from constellixsdk import ConstellixApi
from constellixsdk import IPFilterParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all ipfilters
print("IpFilters:")
ipfilters = constellix.IpFilters.all()
for f in ipfilters:
    if f.name in ["CNSX Test IP Filter", "CNSX Test IP Filter Update"]:
        f.delete()
    print("IpFilter id={}; name={}".format(f.id, f.name))

ipfilters = constellix.IpFilters.all()
initialLen = len(ipfilters)

# create ipfilter
print("Creating IPFilter")
param = IPFilterParam()
param.name = "CNSX Test IP Filter"
param.rulesLimit = 100
param.continents = [IPFilterParam.Continents.AF]
param.countries = [
    "ES",
    "SE",
    "UA"
]

try:
    id = constellix.IpFilters.create_ip_filter(param)
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("IpFilter created with id={}".format(id))

ipfilters = constellix.IpFilters.all()
if initialLen + 1 != len(ipfilters):
    raise Exception("IpFilter Create error")

new_ipfilter = constellix.IpFilters.get_ip_filter(id)
print("New IpFilter id={}; name={}".format(
    new_ipfilter.id, new_ipfilter.name
))
print(new_ipfilter.payload)

# update ipfilter
print("Updating IPFilter")
param = IPFilterParam()
param.name = "CNSX Test IP Filter Update"

updated_ipfilter = new_ipfilter.update(param)
print("Updated IpFilter id={}; name={}".format(
    updated_ipfilter.id, updated_ipfilter.name
))

if updated_ipfilter.name != "CNSX Test IP Filter Update":
    raise Exception("IpFilter Update error")

# delete ipfilter
print("Deleting IPFilter")
new_ipfilter.delete()
ipfilters = constellix.IpFilters.all()
if initialLen != len(ipfilters):
    raise Exception("IpFilter Delete error")
