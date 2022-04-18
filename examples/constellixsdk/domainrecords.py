# Constellix API DomainRecords sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import RecordParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# get Domain object
try:
    domain = constellix.Domains.get_domain(id=100)
except ConstellixApiError as err:
    print(err.message)

# list all domain records
try:
    records = domain.DomainRecords.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of domain records
records = []
cursor = None
while True:
    next_records, cursor = domain.DomainRecords.after(cursor)
    records.extend(next_records)
    if cursor is None:
        break

# create domain record
param = RecordParam()
param.type = RecordParam.Type.A
param.name = "www"
param.value = []
value = RecordParam.RecordValue()
value.enabled = True
value.value = "198.51.100.42"
param.value.append(value)

try:
    new_id = domain.DomainRecords.create_domain_record(param)
except ConstellixApiError as err:
    print(err.message)

# fetch domain record
try:
    new_record = domain.DomainRecords.get_domain_record(new_id)
except ConstellixApiError as err:
    print(err.message)

# update domain record
param = RecordParam()
param.region = RecordParam.Region.EUROPE

try:
    updated_record = new_record.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete domain record
try:
    new_record.delete()
except ConstellixApiError as err:
    print(err.message)
