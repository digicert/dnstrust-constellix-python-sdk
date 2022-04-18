import math
from constellixsdk.api.snapshot import DomainSnapshot


class DomainHistory():
    """
    Managing Domain History endpoint wrapper
    """

    def __init__(self, apiclient, domainid):
        self.__api_client = apiclient
        self.__domain_id = domainid

    def get_history(self):
        """
        Fetches a history of the domain to allow you to see
        when it has changed
        """
        history = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get(
                    "domains/{}/history".format(self.__domain_id)
                )
            else:
                payload = self.__api_client.do_get(
                    "domains/{}/history".format(self.__domain_id),
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                history.append(
                    DomainSnapshot(self.__api_client, self.__domain_id, data)
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

        return history

    def get_history_version(self, version):
        """
        Fetches a single history version for the domain
        """
        payload = self.__api_client.do_get(
            "domains/{}/history/{}".format(self.__domain_id, version)
        )
        return DomainSnapshot(
            self.__api_client,
            self.__domain_id,
            payload["data"]
        )

    def apply_history(self, version):
        """
        Update the domain to the specified version
        in the history of the domain
        """
        self.__api_client.do_post(
            "domains/{}/history/{}/apply".format(self.__domain_id, version)
        )

    def snapshot_history(self, version):
        """
        Snapshot this history version.
        Snapshots are persisted and kept until they are deleted by the user
        """
        self.__api_client.do_post(
            "domains/{}/history/{}/snapshot".format(self.__domain_id, version)
        )
