from constellixsdk.util import parse_payload


class Tag():
    """
    Tag object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current Tag object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("tags/{}".format(self.__id))

    def update(self, tagName):
        """
        Updates the Tag object.
        param:tagName is a new tag name value
        returns updated Tag object
        """
        if not self.__id:
            return None

        payload = payload = "{ \"name\" : \"" + tagName + "\" }"

        result = self.__api_client.do_put(
            "tags/{}".format(self.__id),
            body=payload
        )
        return Tag(self.__api_client, result["data"])

    @property
    def id(self):
        """
        ID for this tag
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        A name for this tag
        """
        try:
            return self.__name
        except AttributeError:
            return None
