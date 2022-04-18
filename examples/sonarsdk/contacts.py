from sonarsdk import SonarApi, SonarApiError

sonar = SonarApi("api_key", "secret_key")

# This call will return the contacts configured within the account.

try:
    contacts = sonar.Contacts.allContacts()
    print("Contacts:")
    for c in contacts:
        print("firstName {}; lastName {}".format(c.firstName, c.lastName))
except SonarApiError as err:
    print(err.message)


# This call returns the configured contact groups within the account.

try:
    groups = sonar.Contacts.allGroups()
    print("Groups:")
    for g in groups:
        print("id {}; name {}".format(g.id, g.name))
except SonarApiError as err:
    print(err.message)
