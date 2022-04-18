from constellixsdk.util import parse_payload, param_to_json
from constellixsdk.api.templaterecords import TemplateRecords


class Template():
    """
    Template object
    """

    def __init__(self, apiclient, payload):
        self.__api_client = apiclient

        self.__id                  = parse_payload(payload, "id")
        self.__name                = parse_payload(payload, "name")
        self.__geoip               = parse_payload(payload, "geoip")
        self.__gtd                 = parse_payload(payload, "gtd")

        self.__template_records = TemplateRecords(self.__api_client, self.__id)
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    @property
    def TemplateRecords(self):
        return self.__template_records

    def delete(self):
        """
        Delete current Template object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete("templates/{}".format(self.__id))

    def update(self, param):
        """
        Updates the Template object.
        param is TemplateParam containing new Template fields
        Returns the updated Template object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "templates/{}".format(self.__id),
            body=payload
        )
        return Template(self.__api_client, result["data"])

    @property
    def id(self):
        """
        The ID of the template object
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name of the template
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def geoip(self):
        """
        Is GeoIP functionality enabled for the template
        """
        try:
            return self.__geoip
        except AttributeError:
            return None

    @property
    def gdt(self):
        """
        Is Global Traffic Director enabled for the template
        """
        try:
            return self.__gtd
        except AttributeError:
            return None
