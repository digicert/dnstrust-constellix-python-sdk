# Constellix API Pools sample usage

from constellixsdk import ConstellixApi, ConstellixApiError
from constellixsdk import PoolParam

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all pools
try:
    pools = constellix.Pools.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of pools
pools = []
cursor = None
while True:
    next_pools, cursor = constellix.Pools.after(cursor)
    pools.extend(next_pools)
    if cursor is None:
        break

# create pool
param = PoolParam()
param.type = PoolParam.Type.A
param.name = "Sample Pool"
param.returnValue = 1
param.enabled = True

poolValue = PoolParam.PoolValue()
poolValue.value = "198.51.100.42"
poolValue.weight = 1000
poolValue.enabled = True
poolValue.handicap = PoolParam.PoolValue.Policy.FOLLOW_SONAR
poolValue.sonarCheckId = 76627
param.values.append(poolValue)

param.ito.enabled = True
param.ito.config.period = PoolParam.PoolItoConfig.Period.PERIOD60
param.ito.config.maximumNumberOfResults = 4
param.ito.config.deviationAllowance =\
    PoolParam.PoolItoConfig.DeviationAllowance.DA90
param.ito.config.monitoringRegion =\
    PoolParam.PoolItoConfig.MonitoringRegion.WORLD
param.ito.config.handicapFactor =\
    PoolParam.PoolItoConfig.HandicapFactor.PERCENT

try:
    new_id = constellix.Pools.create_pool(param)
except ConstellixApiError as err:
    print(err.message)

# fetch pool
try:
    new_pool = constellix.Pools.get_pool(new_id)
except ConstellixApiError as err:
    print(err.message)

# update pool
param = PoolParam()
poolValue = PoolParam.PoolValue()
poolValue.value = "168.0.0.42"
poolValue.weight = 1000
poolValue.enabled = True
poolValue.handicap = PoolParam.PoolValue.Policy.FOLLOW_SONAR
poolValue.sonarCheckId = 76627
param.values.append(poolValue)

try:
    updated_pool = new_pool.update(param)
except ConstellixApiError as err:
    print(err.message)

# delete pool
try:
    new_pool.delete()
except ConstellixApiError as err:
    print(err.message)
