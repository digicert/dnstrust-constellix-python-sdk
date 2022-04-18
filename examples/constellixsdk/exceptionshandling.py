from constellixsdk import ConstellixApi
from constellixsdk.constellixapierror import ConstellixApiError
from constellixsdk.constellixapierror import NotAuthorized
from constellixsdk.constellixapierror import RequestLimitExceeded
from constellixsdk.constellixapierror import RequestCouldNotBeProcessed

constellix = ConstellixApi("your api key", "your secret key")

# Sample Exceptions handling sor Constellix SDK calls

try:
    domains = constellix.Domains.all()
except RequestLimitExceeded as err:
    print(err.message)
except NotAuthorized as err:
    print(err.message)
except RequestCouldNotBeProcessed as err:
    print(err.message)

# Handling general type of exceptions
try:
    domains = constellix.Domains.all()
except ConstellixApiError as err:
    print(err.message)
