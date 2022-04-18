# Constellix API ContactLists sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import ContactListParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all contactlists
try:
    contactlists = constellix.ContactLists.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of contactlists
contactlists = []
cursor = None
while True:
    next_contactlists, cursor = constellix.ContactLists.after(cursor)
    contactlists.extend(next_contactlists)
    if cursor is None:
        break

# create contactlist
param = ContactListParam()
param.name = "Contact List Name"
param.emails = [
    "bob@example.com",
    "alice@example.com"
]

try:
    new_id = constellix.ContactLists.create_contact_list(param)
except ConstellixApiError as err:
    print(err.message)

# fetch contactlist
try:
    new_contactlist = constellix.ContactLists.get_contact_list(new_id)
except ConstellixApiError as err:
    print(err.message)

# update contactlist
param = ContactListParam()
param.name = "New Contact List Name"
param.emails = [
    "bob@example.com",
    "alice@example.com",
    "tom@example.com"
]

try:
    updated_contactlist = new_contactlist.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete contactlist
try:
    new_contactlist.delete()
except ConstellixApiError as err:
    print(err.message)
