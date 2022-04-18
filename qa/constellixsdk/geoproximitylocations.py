from constellixsdk import ConstellixApi
from constellixsdk import GeoProximityParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all domain
print("Geo Proximity Locations:")
geoproximities = constellix.GeoProximities.all()
for g in geoproximities:
    print("Geo Proximity id={}; name={}".format(g.id, g.name))
    if g.name in [
        "CNSX QA Test Geo Proximity Location",
        "CNSX QA Update Geo Proximity Location"
    ]:
        g.delete()

geoproximities = constellix.GeoProximities.all()
initialLen = len(geoproximities)

# create geo proximity
print("Create Geo Proximity")

param = GeoProximityParam()
param.name = "CNSX QA Test Geo Proximity Location"
param.longitude = 22.7
param.latitude = 56.8333

try:
    new_id = constellix.GeoProximities.create_geo_proximity(param)
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("New id= {}".format(new_id))

new_gpl = constellix.GeoProximities.get_geo_proximity(new_id)
print("New Geo Proximity id={}; name={}".format(new_gpl.id, new_gpl.name))

geoproximities = constellix.GeoProximities.all()
if initialLen + 1 != len(geoproximities):
    raise Exception("Create Geo Proximity error")

# update Geo Proximity
print("Update Geo Proximity")
param = GeoProximityParam()
param.name = "CNSX QA Update Geo Proximity Location"

try:
    up_gpl = new_gpl.update(param)
except Exception as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

# delete Geo Proximity
print("Delete Geo Proximity")
new_gpl.delete()

geoproximities = constellix.GeoProximities.all()
if initialLen != len(geoproximities):
    raise Exception("Delete Geo Proximity error")
