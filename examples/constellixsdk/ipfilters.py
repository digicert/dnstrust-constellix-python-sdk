# Constellix API IpFilters sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import IPFilterParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all ipfilters
try:
    ipfilters = constellix.IpFilters.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of ipfilters
ipfilters = []
cursor = None
while True:
    next_ipfilters, cursor = constellix.IpFilters.after(cursor)
    ipfilters.extend(next_ipfilters)
    if cursor is None:
        break

# create ipfilter
param = IPFilterParam()
param.name = "Sample IP Filter"
param.rulesLimit = 100
param.continents = [IPFilterParam.Continents.EU, IPFilterParam.Continents.NA]
param.countries = [
    "GB",
    "PL",
    "RO"
]
param.ipv4 = [
    "198.51.100.0/24",
    "203.0.113.42"
]
param.ipv6 = [
    "2001:db8:200::/64",
    "2001:db8:200:42::"
]

try:
    new_id = constellix.IpFilters.create_ip_filter(param)
except ConstellixApiError as err:
    print(err.message)

# fetch ipfilter
try:
    new_ipfilter = constellix.IpFilters.get_ip_filter(new_id)
except ConstellixApiError as err:
    print(err.message)

# update ipfilter
param = IPFilterParam()
param.ipv4 = [
    "128.61.100.0/24",
    "196.0.113.42",
    "247.0.56.30"
]

try:
    updated_ipfier = new_ipfilter.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete ipfilter
try:
    new_ipfilter.delete()
except ConstellixApiError as err:
    print(err.message)
