# Constellix API Announcements sample usage

from constellixsdk import ConstellixApi, ConstellixApiError

# create Constellix API entry point object
constellix = ConstellixApi(apikey="API-KEY", secret="SECRET-KEY")

# list all announcements
try:
    announcements = constellix.Announcements.all()
except ConstellixApiError as err:
    print(err.message)

# Cursor pagination of announcements
announcements = []
cursor = None
while True:
    next_announcements, cursor = constellix.Announcements.after(cursor)
    announcements.extend(next_announcements)
    if cursor is None:
        break

# fetch single announcement
try:
    announcement = constellix.Announcements.get_announcement(id = 111)
except ConstellixApiError as err:
    print(err.message)
