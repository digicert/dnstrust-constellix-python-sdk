from constellixsdk import ConstellixApi, ConstellixApiError

# create Constellix API entry point object
constellix = ConstellixApi()

# list all Tags
print("Tags:")
tags = constellix.Tags.all()
for t in tags:
    print("Tag id={}; name={}".format(t.id, t.name))
    if t.name in ["CNSX QA Tag", "CNSX QA Tag U"]:
        t.delete()

tags = constellix.Tags.all()
initialLen = len(tags)

# create Tag
print("Creating Tag")
try:
    new_id = constellix.Tags.create_tag("CNSX QA Tag")
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Tag created with id={}".format(new_id))

tags = constellix.Tags.all()
if initialLen + 1 != len(tags):
    raise Exception("Tag Create error")

new_tag = constellix.Tags.get_tag(new_id)
print("New Tag id={}; name={}".format(new_tag.id, new_tag.name))

# update Tag
print("Updating Tag")
try:
    updated_tag = new_tag.update("CNSX QA Tag U")
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Updated Tag id={}; name={}".format(updated_tag.id, updated_tag.name))
if updated_tag.name != "CNSX QA Tag U":
    raise Exception("Tag Update error")

# delete Tag
print("Deleting Tag")
try:
    updated_tag.delete()
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

tags = constellix.Tags.all()
if initialLen != len(tags):
    raise Exception("Tag Delete error")
