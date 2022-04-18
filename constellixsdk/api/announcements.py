import math
from constellixsdk.api.announcement import Announcement


class Announcements():
    """
    Managing Announcements endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns A list of all announcements
        """
        announcements = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("announcements")
            else:
                payload = self.__api_client.do_get(
                    "announcements", params={"page": currentPage})
            for data in payload["data"]:
                announcements.append(Announcement(self.__api_client, data))
            totalPages = 1
            try:
                totalPages = payload["meta"]["pagination"]["totalPages"]
            except:
                totalPages = math.ceil(
                    payload["meta"]["pagination"]["total"] /
                    payload["meta"]["pagination"]["perPage"]
                )
            if payload["meta"]["pagination"]["currentPage"] >= totalPages:
                break
            currentPage = payload["meta"]["pagination"]["currentPage"] + 1

        return announcements

    def after(self, cursor):
        """
        Cursor pagination for announcement objects
        """
        announcements = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("announcements")
        else:
            payload = self.__api_client.do_get(
                "announcements", params={"page": currentPage}
            )

        for data in payload["data"]:
            announcements.append(Announcement(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return announcements, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return announcements, cursor

    def get_announcement(self, id):
        """
        Fetches a single announcement
        """
        payload = self.__api_client.do_get("announcements/{}".format(id))
        return Announcement(self.__api_client, payload["data"])
