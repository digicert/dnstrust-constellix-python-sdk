# Constellix API GeoProximities sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import GeoProximityParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all geoproximities
try:
    geoproximities = constellix.GeoProximities.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of geoproximities
geoproximities = []
cursor = None
while True:
    next_geoproximities, cursor = constellix.GeoProximities.after(cursor)
    geoproximities.extend(next_geoproximities)
    if cursor is None:
        break

# create geoproximity
param = GeoProximityParam()
param.name = "Sample Geo Proximity Location"
param.longitude = 22.7
param.latitude = 56.8333

try:
    new_id = constellix.GeoProximities.create_geo_proximity(param)
except ConstellixApiError as err:
    print(err.message)

# fetch geoproximity
try:
    new_geoproximity = constellix.GeoProximities.get_geo_proximity(new_id)
except ConstellixApiError as err:
    print(err.message)

# update geoproximity
param = GeoProximityParam()
param.country = "GB"
param.region = "London"
param.city = "London"

try:
    updated_geoproximity = new_geoproximity.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete geoproximity
try:
    new_geoproximity.delete()
except ConstellixApiError as err:
    print(err.message)
