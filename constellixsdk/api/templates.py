import math
from constellixsdk.api.template import Template
from constellixsdk.util import param_to_json


class TemplateParam():
    """
    Template param for Create and Update operations
    """

    def __init__(self):
        # string : The name of the template
        self.name = ""

        # boolean : Is GeoIP functionality enabled for the template
        self.geoip = None

        # boolean : Is Global Traffic Director enabled for the template
        self.gtd = None
        pass


class Templates():
    """
    Managing Templates endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all Templates in the account
        """
        templates = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("templates")
            else:
                payload = self.__api_client.do_get(
                    "templates",
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                templates.append(Template(self.__api_client, data))
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

        return templates

    def after(self, cursor):
        """
        Cursor pagination for Template objects
        """
        templates = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("templates")
        else:
            payload = self.__api_client.do_get(
                "templates",
                params={"page": currentPage}
            )

        for data in payload["data"]:
            templates.append(Template(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return templates, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return templates, cursor

    def get_template(self, id):
        """
        Fetches a single Template in your account
        """
        result = self.__api_client.do_get("templates/{}".format(id))
        return Template(self.__api_client, result["data"])

    def create_template(self, param):
        """
        Creates a new Template in your account.
        param is TeemplateParam containing new Template fields
        Returns the id of created Template
        """

        payload = param_to_json(param)

        result = self.__api_client.do_post("templates", body=payload)
        return result["data"]["id"]
