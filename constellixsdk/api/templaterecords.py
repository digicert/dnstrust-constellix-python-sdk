import math
from constellixsdk.api.templaterecord import TemplateRecord
from constellixsdk.util import param_to_json


class TemplateRecords():
    """
    Managing TemplateRecords endpoint wrapper
    """

    def __init__(self, apiclient, templateid):
        self.__api_client = apiclient
        self.__template_id = templateid

    def all(self):
        """
        Returns a list of all TemplateRecords in the Template
        """
        templaterecords = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get(
                    "templates/{}/records".format(self.__template_id)
                )
            else:
                payload = self.__api_client.do_get(
                    "templates/{}/records".format(self.__template_id),
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                templaterecords.append(
                    TemplateRecord(self.__api_client, self.__template_id, data)
                )
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

        return templaterecords

    def after(self, cursor):
        """
        Cursor pagination for TemplateRecord objects
        """
        templaterecords = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get(
                "templates/{}/records".format(self.__template_id)
            )
        else:
            payload = self.__api_client.do_get(
                "templates/{}/records".format(self.__template_id),
                params={"page": currentPage}
            )

        for data in payload["data"]:
            templaterecords.append(
                TemplateRecord(self.__api_client, self.__template_id, data)
            )

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return templaterecords, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return templaterecords, cursor

    def get_template_record(self, id):
        """
        Fetches a single TemplateRecords in Template
        """
        result = self.__api_client.do_get(
            "templates/{}/records/{}".format(self.__template_id, id)
        )
        return TemplateRecord(
            self.__api_client,
            self.__template_id,
            result["data"]
        )

    def create_template_record(self, param):
        """
        Creates a new TemplateRecords in Template
        param is RecordParam containing new TemplateRecords fields
        Returns the ID of created TemplateRecord object
        """

        payload = param_to_json(param)

        result = self.__api_client.do_post(
            "templates/{}/records".format(self.__template_id),
            body=payload
        )
        return result["data"]["id"]
