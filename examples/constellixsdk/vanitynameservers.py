# Constellix API VanityNameservers sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import VanityNameserverParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all vanitynameservers
try:
    vanitynameservers = constellix.VanityNameservers.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of vanitynameservers
vanitynameservers = []
cursor = None
while True:
    next_vanitynameservers, cursor = constellix.VanityNameservers.after(cursor)
    vanitynameservers.extend(next_vanitynameservers)
    if cursor is None:
        break

# create vanitynameserver
param = VanityNameserverParam()
param.name = "Sample Vanity Nameserver"
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
    print(err.message)

# fetch vanitynameserver
try:
    new_vanitynameserver = constellix.VanityNameservers.get_vanity_nameserver(
        new_id
    )
except ConstellixApiError as err:
    print(err.message)

# update vanitynameserver
param = VanityNameserverParam()
param.default = False

try:
    updated_vanitynameserver = new_vanitynameserver.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete vanitynameserver
try:
    new_vanitynameserver.delete()
except ConstellixApiError as err:
    print(err.message)
