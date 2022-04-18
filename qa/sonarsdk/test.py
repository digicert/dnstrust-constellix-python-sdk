from sonarsdk import SonarApi, SonarApiError

sonar = SonarApi()

try:
    check = sonar.HTTPChecks.get_http_check(id = 64766)
except SonarApiError as err:
    print(err.message)
    print(err.response.status_code)
    print(err.response.text)
print(check.name)
print(check.payload)

try:
    print("Check State")
    print(check.check_state())
except SonarApiError as err:
    print(err.message)
    print(err.response.status_code)
    print(err.response.text)

try:
    print("Check Status")
    print(check.check_status())
except SonarApiError as err:
    print(err.message)
    print(err.response.status_code)
    print(err.response.text)
