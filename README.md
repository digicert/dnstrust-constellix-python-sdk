# Python SDK for Constellix API v4


# Setup
In order to get this SDK works for python, you need to get installed:
PIP, setuptools and requests

To install dnsmesdk package locally, go to package root directory and execute the next command:

python2:
```
python setup.py install --old-and-unmanageable
```
python3:
```
python3 setup.py install --old-and-unmanageable
```

# Usage Examples

Setting apikey and secretkey over environment variables

```
export CONSTELLIX_API_KEY=<api_key>
export CONSTELLIX_SECRET_KEY=<secret_key>
```

```python
from constellixsdk import ConstellixApi
from sonarsdk import SonarApi

constellix = ConstellixApi()
sonar = SonarApi()
```

Passing apikey and secretkey to ConstellixApi and SonarApi objects

```python
from constellixsdk import ConstellixApi
from sonarsdk import SonarApi

constellix = ConstellixApi("api_key", "secret_key")
sonar = SonarApi("api_key", "secret_key")
```

Please check examples folder for sample usages
