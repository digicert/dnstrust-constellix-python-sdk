from constellixsdk.util import parse_payload, param_to_json


class TemplateRecord():
    """
    Template Record object
    """

    def __init__(self, apiclient, templateid, payload):
        self.__api_client = apiclient
        self.__template_id = templateid

        self.__id                  = parse_payload(payload, "id")
        self.__type                = parse_payload(payload, "type")
        self.__ttl                 = parse_payload(payload, "ttl")
        self.__enabled             = parse_payload(payload, "enabled")
        self.__name                = parse_payload(payload, "name")
        self.__region              = parse_payload(payload, "region")
        try:
            self.__ipfilterId      = parse_payload(payload, "ipfilter")["id"]
        except:
            self.__ipfilterId = None
        try:
            self.__geoproximityId  = parse_payload(
                payload,
                "geoproximity"
            )["id"]
        except:
            self.__geoproximityId = None
        self.__ipfilterDrop        = parse_payload(payload, "ipfilterDrop")
        self.__notes               = parse_payload(payload, "notes")
        try:
            self.__contactsId      = parse_payload(payload, "contacts")["id"]
        except:
            self.__contactsId = None
        self.__mode                = parse_payload(payload, "mode")
        self.__value               = parse_payload(payload, "value")
        self.__lastValues          = parse_payload(payload, "lastValues")
        try:
            self.__templateId      = parse_payload(payload, "template")["id"]
        except:
            self.__templateId = None
        self.__payload = payload

    @property
    def payload(self):
        """
        Original payload of the object
        """
        return self.__payload

    def delete(self):
        """
        Delete current TemplateRecord object
        """
        if not self.__id:
            return None

        self.__api_client.do_delete(
            "templates/{}/records/{}".format(self.__template_id, self.__id)
        )

    def update(self, param):
        """
        Updates the TemplateRecord object.
        param is RecordParam containing new TemplateRecord fields
        Returns updated TemplateRecord object
        """
        if not self.__id:
            return None

        payload = param_to_json(param)

        result = self.__api_client.do_put(
            "templates/{}/records/{}".format(self.__template_id, self.__id),
            body=payload
        )
        return TemplateRecord(
            self.__api_client,
            self.__template_id,
            result["data"]
        )

    @property
    def id(self):
        """
        The ID of the template record object
        """
        try:
            return self.__id
        except AttributeError:
            return None

    @property
    def type(self):
        """
        The type of record
        """
        try:
            return self.__type
        except AttributeError:
            return None

    @property
    def ttl(self):
        """
        How long DNS servers should cache the record for
        """
        try:
            return self.__ttl
        except AttributeError:
            return None

    @property
    def enabled(self):
        """
        Whether the record is enabled
        """
        try:
            return self.__enabled
        except AttributeError:
            return None

    @property
    def name(self):
        """
        The name for the record
        """
        try:
            return self.__name
        except AttributeError:
            return None

    @property
    def region(self):
        """
        Optional region for this record. Will default to 'default'.
        """
        try:
            return self.__region
        except AttributeError:
            return None

    @property
    def ipfilterId(self):
        """
        The integer ID of an IP Filter to use for this record
        """
        try:
            return self.__ipfilterId
        except AttributeError:
            return None

    @property
    def geoproximityId(self):
        """
        The integer ID of a GeoProximity to use for this record
        """
        try:
            return self.__geoproximityId
        except AttributeError:
            return None

    @property
    def ipfilterDrop(self):
        """

        """
        try:
            return self.__ipfilterDrop
        except AttributeError:
            return None

    @property
    def notes(self):
        """
        A description of the record
        """
        try:
            return self.__notes
        except AttributeError:
            return None

    @property
    def contactsId(self):
        """

        """
        try:
            return self.__contactsId
        except AttributeError:
            return None

    @property
    def mode(self):
        """

        """
        try:
            return self.__mode
        except AttributeError:
            return None

    @property
    def value(self):
        """

        """
        try:
            return self.__value
        except AttributeError:
            return None

    @property
    def lastValues(self):
        """

        """
        try:
            return self.__lastValues
        except AttributeError:
            return None

    @property
    def templateId(self):
        """

        """
        try:
            return self.__templateId
        except AttributeError:
            return None
