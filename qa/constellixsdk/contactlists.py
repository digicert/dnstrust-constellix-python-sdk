from constellixsdk import ConstellixApi
from constellixsdk import ContactListParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all Contact Lists
print("Contact Lists:")
try:
    clists = constellix.ContactLists.all()
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

for c in clists:
    print("Contact id={}; name={}".format(c.id, c.name))
initialLen = len(clists)

# create Contact List
print("Creating Contact List")
param = ContactListParam()
param.name = "CNSX QA Test Contact List"
param.emails = [
    "bob@example.com",
    "alice@example.com"
]

try:
    new_id = constellix.ContactLists.create_contact_list(param)
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Contact List created with id={}".format(new_id))

new_clist = constellix.ContactLists.get_contact_list(new_id)
print("New Contact List id={}; name={}".format(new_clist.id, new_clist.name))

clists = constellix.ContactLists.all()
if initialLen + 1 != len(clists):
    raise Exception("Contact List Create error")

# Update Contact List
print("Updating Contact List")
param = ContactListParam()
param.name = "CNSX QA Update Contact List"

try:
    updated_clist = new_clist.update(param)
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

# delete Contact List
print("Deleting Contact List")
new_clist.delete()

clists = constellix.ContactLists.all()
if initialLen != len(clists):
    raise Exception("Contact List Delete error")
