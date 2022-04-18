from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import RecordParam
from constellixsdk import TemplateParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all templates
print("Templates:")
templates = constellix.Templates.all()
for t in templates:
    print("Template id={}; name={}".format(t.id, t.name))
    if t.name in ["CNSX Test Template", "CNSX Test Template Update"]:
        t.delete()

# create template
param = TemplateParam()
param.name = "CNSX Test Template"
param.geoip = True
param.gtd = True

try:
    id = constellix.Templates.create_template(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Template created with id={}".format(id))

new_template = constellix.Templates.get_template(id)
print("New Template id={}; name={}".format(new_template.id, new_template.name))

# list template records
print("Template records:")
try:
    records = new_template.TemplateRecords.all()
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

recordsTotal = len(records)

# create template record
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

record_id = new_template.TemplateRecords.create_template_record(param)
print("New Template Record id={}".format(record_id))

new_record = new_template.TemplateRecords.get_template_record(record_id)
print("New Template Record id={}; name={}; type={}".format(
    new_record.id, new_record.name, new_record.type
))

# update record
print("Updating Template Record")
param = RecordParam()
param.enabled = False

try:
    updated_record = new_record.update(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

if updated_record.enabled is not False:
    raise Exception("Template Record Update error")

# deleting
print("Deleting Template Record")
new_record.delete()
records = new_template.TemplateRecords.all()
if recordsTotal != len(records):
    raise Exception("Delete Template Record Error")

# delete template
print("Deleting Template")
new_template.delete()
