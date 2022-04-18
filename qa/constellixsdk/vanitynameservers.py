from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import VanityNameserverParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all Vanity Nameservers
print("Vanity Nameservers:")
try:
    vanities = constellix.VanityNameservers.all()
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

for v in vanities:
    print("Vanity id={}; name={}".format(v.id, v.name))
    if v.name in ["CNSX QA Test Vanity Nameserver"]:
        v.delete()

vanities = constellix.VanityNameservers.all()
initialLen = len(vanities)

# create Vanity Nameserver
print("Creating Vanity Nameserver")
param = VanityNameserverParam()
param.name = "CNSX QA Test Vanity Nameserver"
param.default = False
param.nameserverGroup.id = 1
param.nameserverGroup.name = "Nameserver Group 1"
param.nameservers = [
    "ns1.example.com",
    "ns2.example.com"
]

try:
    new_id = constellix.VanityNameservers.create_vanity_nameserver(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Vanity created with id={}".format(new_id))

new_vanity = constellix.VanityNameservers.get_vanity_nameserver(new_id)
print("New Vanity id={}; name={}".format(new_vanity.id, new_vanity.name))

vanities = constellix.VanityNameservers.all()
if initialLen + 1 != len(vanities):
    raise Exception("Vanity Nameserver Create error")


# update vanity
print("Updating Vanity Nameserver")
param = VanityNameserverParam()
param.name = "CNSX QA Test Vanity Update"

updated_vanity = new_vanity.update(param)
if updated_vanity.name != "CNSX QA Test Vanity Update":
    raise Exception("Vanity Nameserver Update Error")

# delete Vanity
print("Deleting Vanity Nameserver")
new_vanity.delete()

vanities = constellix.VanityNameservers.all()
if initialLen != len(vanities):
    raise Exception("Vanity Nameserver Delete error")
