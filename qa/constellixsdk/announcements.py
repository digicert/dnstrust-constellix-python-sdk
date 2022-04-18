from constellixsdk import ConstellixApi

# create Constellix API entry point object
constellix = ConstellixApi()

# list all Announcements
print("Announcements:")
try:
    alist = constellix.Announcements.all()
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

for a in alist:
    print("Announcement id={}; name={}".format(a.id, a.title))
initialLen = len(alist)
