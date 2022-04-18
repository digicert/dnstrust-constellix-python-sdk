from constellixsdk.util import parse_payload, param_to_json


class GeoProximity():
    """
    GeoProximity object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__country             = parse_payload(payload, "country")
        self.__region              = parse_payload(payload, "region")
        self.__city                = parse_payload(payload, "city")
        self.__longitude           = parse_payload(payload, "longitude")
        self.__latitude            = parse_payload(payload, "latitude")
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current GeoProximity object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("geoproximities/{}".format(self.__id))

    def update(self, param):
        """
        Updates the GeoProximity object.
        param is GeoProximityParam containing new GeoProximity fields
        Returns updated GeoProximity object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "geoproximities/{}".format(self.__id),
            body=payload
        )
        return GeoProximity(self.__api_client, result["data"])

    @property
    def id(self):
        """
        The ID of the Geo Proximity location
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name of the Geo Proximity location
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def country(self):
        """
        2 digit ISO country code
        """
        try:
            return self.__country
        except AttributeError:
            return None

    @property
    def region(self):
        """
        Region, state or province code
        """
        try:
            return self.__region
        except AttributeError:
            return None

    @property
    def city(self):
        """
        The numeric ID for a city
        """
        try:
            return self.__city
        except AttributeError:
            return None

    @property
    def longitude(self):
        """
        Longitude of the location
        """
        try:
            return self.__longitude
        except AttributeError:
            return None

    @property
    def latitude(self):
        """
        Latitude of the location
        """
        try:
            return self.__latitude
        except AttributeError:
            return None
