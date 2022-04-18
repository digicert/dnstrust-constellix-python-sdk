import math
from constellixsdk.api.tag import Tag


class Tags():
    """
    Managing Tags endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all Tags in the account
        """
        tags = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("tags")
            else:
                payload = self.__api_client.do_get(
                    "tags",
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                tags.append(Tag(self.__api_client, data))
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

        return tags

    def after(self, cursor):
        """
        Cursor pagination for Tag objects
        """
        tags = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("tags")
        else:
            payload = self.__api_client.do_get(
                "tags",
                params={"page": currentPage}
            )

        for data in payload["data"]:
            tags.append(Tag(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return tags, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return tags, cursor

    def get_tag(self, id):
        """
        Fetches a single Tag in your account
        """
        payload = self.__api_client.do_get("tags/{}".format(id))
        return Tag(self.__api_client, payload["data"])

    def create_tag(self, tagName):
        """
        Creates a new Tag in your account.
        param:tagName is a new tag name
        returns id of created tag object
        """
        payload = "{ \"name\" : \"" + tagName + "\" }"

        result = self.__api_client.do_post("tags", body=payload)
        return result["data"]["id"]
