# Constellix API Tags sample usage

from constellixsdk import ConstellixApi, ConstellixApiError

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all tags
try:
    tags = constellix.Tags.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of tags
tags = []
cursor = None
while True:
    next_tags, cursor = constellix.Tags.after(cursor)
    tags.extend(next_tags)
    if cursor is None:
        break

# create tag
try:
    new_id = constellix.Tags.create_tag("new-tag")
except ConstellixApiError as err:
    print(err.message)

# fetch tag
try:
    new_tag = constellix.Tags.get_tag(new_id)
except ConstellixApiError as err:
    print(err.message)

# update tag
try:
    updated_tag = new_tag.update("updated-tag")
except ConstellixApiError as err:
    print(err.message)

# delete tag
try:
    new_tag.delete()
except ConstellixApiError as err:
    print(err.message)
