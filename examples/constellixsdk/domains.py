# Constellix API Domains sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import DomainParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all domain
try:
    domains = constellix.Domains.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of domains
domains = []
cursor = None
while True:
    next_domains, cursor = constellix.Domains.after(cursor)
    domains.extend(next_domains)
    if cursor is None:
        break

# create domain
param = DomainParam()
param.name = "domain.com"
param.soa.primaryNameserver = "ns11.constellix.com"
param.soa.email = "admin.example.com"
param.soa.ttl = 86400
param.soa.refresh = 86400
param.soa.retry = 7200
param.soa.expire = 3600000
param.soa.negativeCache = 180
param.note = "Sample Domain"
param.geoip = True
param.gtd = True

try:
    new_id = constellix.Domains.create_domain(param)
except ConstellixApiError as err:
    print(err.message)

# fetch domain
try:
    new_domain = constellix.Domains.get_domain(new_id)
except ConstellixApiError as err:
    print(err.message)

# update domain
param = DomainParam()
param.soa.primaryNameserver = "ns12.constellix.com"
param.soa.email = "admin.email.com"

try:
    updated_domain = new_domain.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete domain
try:
    new_domain.delete()
except ConstellixApiError as err:
    print(err.message)
