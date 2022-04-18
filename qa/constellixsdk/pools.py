from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import PoolParam

# create Constellix API entry point object
constellix = ConstellixApi()

# list all pools
print("Pools:")

try:
    pools = constellix.Pools.all()
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

for p in pools:
    print("Pool id={}; name={}".format(p.id, p.name))
    if p.name in ["CNSX Test Pool", "CNSX Test Pool Update"]:
        p.delete()

pools = constellix.Pools.all()
initialLen = len(pools)

# create pool
print("Creating Pool")
param = PoolParam()
param.type = PoolParam.Type.A
param.name = "CNSX Test Pool"
param.returnValue = 1
param.enabled = True

poolValue = PoolParam.PoolValue()
poolValue.value = "198.51.100.42"
poolValue.weight = 1000
poolValue.enabled = True
poolValue.handicap = 10
poolValue.policy = PoolParam.PoolValue.Policy.ALWAYS_OFF
param.values.append(poolValue)

param.ito.enabled = False
param.ito.config.period = PoolParam.PoolItoConfig.Period.PERIOD60
param.ito.config.maximumNumberOfResults = 1
param.ito.config.deviationAllowance =\
    PoolParam.PoolItoConfig.DeviationAllowance.DA90
param.ito.config.monitoringRegion =\
    PoolParam.PoolItoConfig.MonitoringRegion.WORLD
param.ito.config.handicapFactor =\
    PoolParam.PoolItoConfig.HandicapFactor.PERCENT

try:
    id = constellix.Pools.create_pool(param)
except ConstellixApiError as err:
    print(err.message)
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

print("Pool created with id={}".format(id))

pools = constellix.Pools.all()
if initialLen + 1 != len(pools):
    raise Exception("Pool Create error")

new_pool = constellix.Pools.get_pool(id, "A")
print("New Pool id={}; name={}".format(new_pool.id, new_pool.name))

# update pool
print("Updating Pool")
param = PoolParam()
param.name = "CNSX Test Pool Update"

print("Updating pool")

try:
    updated_pool = new_pool.update(param)
except ConstellixApiError as err:
    print("URL {}".format(constellix.last_request_url))
    print("Body {}".format(constellix.last_request_body))
    print("Response Status code {}".format(
        constellix.last_response.status_code
    ))
    print("Response Text {}".format(constellix.last_response.text))
    raise err

if updated_pool.name != "CNSX Test Pool Update":
    raise Exception("Pool Update error")

# delete pool
print("Deleting pool")
updated_pool.delete()
pools = constellix.Pools.all()
if initialLen != len(pools):
    raise Exception("Pool Delete error")
