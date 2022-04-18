from sonarsdk import SonarApi
from sonarsdk.sonarapierror import SonarApiError
from sonarsdk.sonarapierror import RequestLimitExceeded
from sonarsdk.sonarapierror import RequestCouldNotBeProcessed
from sonarsdk.sonarapierror import NotAuthorized

sonar = SonarApi("your api key", "your secret key")

# Sample Exceptions handling sor Sonar SDK calls

try:
    agents = sonar.Agents.all()
except RequestLimitExceeded as err:
    print(err.message)
except NotAuthorized as err:
    print(err.message)
except RequestCouldNotBeProcessed as err:
    print(err.message)

# Handling general type of exceptions
try:
    agents = sonar.Agents.all()
except SonarApiError as err:
    print(err.message)
