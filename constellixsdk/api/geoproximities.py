import math
from constellixsdk.api.geoproximity import GeoProximity
from constellixsdk.util import param_to_json


class GeoProximityParam():
    """
    Param for GeoProximity Create and Update operations
    """

    def __init__(self):

        # string : The name of the Geo Proximity location
        self.name = ""

        # string : 2 digit ISO country code
        self.country = ""

        # string : Region, state or province code
        self.region = ""

        # integer : The numeric ID for a city
        self.city = None

        # float : Longitude of the location
        self.longitude = None

        # float : Latitude of the location
        self.latitude = None
        pass


class GeoProximities():
    """
    Managing GeoProximities endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all GeoProximities in the account
        """
        geoproximities = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("geoproximities")
            else:
                payload = self.__api_client.do_get(
                    "geoproximities", params={"page": currentPage}
                )
            for data in payload["data"]:
                geoproximities.append(GeoProximity(self.__api_client, data))
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

        return geoproximities

    def after(self, cursor):
        """
        Cursor pagination for GeoProximity objects
        """
        geoproximities = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("geoproximities")
        else:
            payload = self.__api_client.do_get(
                "geoproximities",
                params={"page": currentPage}
            )

        for data in payload["data"]:
            geoproximities.append(GeoProximity(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return geoproximities, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return geoproximities, cursor

    def get_geo_proximity(self, id):
        """
        Fetches a single GeoProximity in your account
        """
        result = self.__api_client.do_get("geoproximities/{}".format(id))
        return GeoProximity(self.__api_client, result["data"])

    def create_geo_proximity(self, param):
        """
        Creates a new GeoProximity in your account.
        param is GeoProximityParam containing new GeoProximity fields
        Returns the id of created GeoProximity
        """

        payload = param_to_json(param)

        result = self.__api_client.do_post("geoproximities", body=payload)
        return result["data"]["id"]
