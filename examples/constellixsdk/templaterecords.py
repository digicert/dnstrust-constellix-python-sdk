# Constellix API TemplateRecords sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import RecordParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# get Template object
try:
    template = constellix.Templates.get_template(id=100)
except ConstellixApiError as err:
    print(err.message)

# list all Template records
try:
    records = template.TemplateRecords.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of template records
records = []
cursor = None
while True:
    next_records, cursor = template.TemplateRecords.after(cursor)
    records.extend(next_records)
    if cursor is None:
        break

# create Template record
param = RecordParam()
param.type = RecordParam.Type.A
param.name = "www"
param.enabled = True
param.ttl = 60
param.notes = "This is my A record"
param.region = RecordParam.Region.EUROPE
param.mode = RecordParam.Mode.STANDARD
param.value = []

value = RecordParam.RecordValue()
value.enabled = True
value.value = "198.51.100.42"
param.value.append(value)

try:
    new_id = template.TemplateRecords.create_template_record(param)
except ConstellixApiError as err:
    print(err.message)

# fetch Template record
try:
    new_record = template.TemplateRecords.get_template_record(new_id)
except ConstellixApiError as err:
    print(err.message)

# update Template record
param = RecordParam()
param.value = []

value = RecordParam.RecordValue()
value.enabled = True
value.value = "198.51.100.42"
param.value.append(value)

value = RecordParam.RecordValue()
value.enabled = True
value.value = "168.1.121.65"
param.value.append(value)

try:
    updated_record = new_record.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete Template record
try:
    new_record.delete()
except ConstellixApiError as err:
    print(err.message)
