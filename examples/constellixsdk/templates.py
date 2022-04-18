# Constellix API Templates sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import TemplateParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all template
try:
    templates = constellix.Templates.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of templates
templates = []
cursor = None
while True:
    next_templates, cursor = constellix.Templates.after(cursor)
    templates.extend(next_templates)
    if cursor is None:
        break

# create template
param = TemplateParam()
param.name = "Sample Template"
param.geoip = True
param.gtd = True

try:
    new_id = constellix.Templates.create_template(param)
except ConstellixApiError as err:
    print(err.message)

# fetch template
try:
    new_template = constellix.Templates.get_template(new_id)
except ConstellixApiError as err:
    print(err.message)

# update template
param = TemplateParam()
param.geoip = False
param.gtd = False

try:
    updated_template = new_template.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete template
try:
    new_template.delete()
except ConstellixApiError as err:
    print(err.message)
