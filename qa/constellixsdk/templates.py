from constellixsdk import ConstellixApi, ConstellixApiError
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

templates = constellix.Templates.all()
initialLen = len(templates)

# create template
print("Creating Template")
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

templates = constellix.Templates.all()
if initialLen + 1 != len(templates):
    raise Exception("Template Create error")

new_template = constellix.Templates.get_template(id)
print("New Template id={}; name={}".format(
    new_template.id, new_template.name
))

# update template
print("Updating Template")
param = TemplateParam()
param.name = "CNSX Test Template Update"

try:
    updated_template = new_template.update(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Updated Template id={}; name={}".format(
    updated_template.id, updated_template.name
))

if updated_template.name != "CNSX Test Template Update":
    raise Exception("Template Update error")

# delete template
print("Deleting Template")
updated_template.delete()
templates = constellix.Templates.all()
if initialLen != len(templates):
    raise Exception("Template Delete error")
