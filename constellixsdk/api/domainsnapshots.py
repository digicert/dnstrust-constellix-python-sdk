import math
from constellixsdk.api.snapshot import DomainSnapshot


class DomainSnapshots():
    """
    Managing Domain Snapshots endpoint wrapper
    """

    def __init__(self, apiclient, domainid):
        self.__api_client = apiclient
        self.__domain_id = domainid

    def all(self):
        """
        Fetches saved snapshots of the history the domain
        to allow you to see when it has changed
        """
        snapshots = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get(
                    "domains/{}/snapshots".format(self.__domain_id)
                )
            else:
                payload = self.__api_client.do_get(
                    "domains/{}/snapshots".format(self.__domain_id),
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                snapshots.append(
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

        return snapshots

    def after(self, cursor):
        """
        Cursor pagination for DomainSnapshot objects
        """
        snapshots = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get(
                "domains/{}/snapshots".format(self.__domain_id)
            )
        else:
            payload = self.__api_client.do_get(
                "domains/{}/snapshots".format(self.__domain_id),
                params={"page": currentPage}
            )

        for data in payload["data"]:
            snapshots.append(
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
            return snapshots, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return snapshots, cursor

    def getSnapshot(self, version):
        """
        Fetches a single snapshot for the domain
        """
        payload = self.__api_client.do_get(
            "domains/{}/snapshots/{}".format(self.__domain_id, version)
        )
        return DomainSnapshot(
            self.__api_client,
            self.__domain_id,
            payload["data"]
        )

    def applySnapshot(self, version):
        """
        Update the domain to the specified snapshot
        in the history of the domain
        """
        self.__api_client.do_post(
            "domains/{}/snapshots/{}/apply".format(self.__domain_id, version)
        )

    def deleteSnapshot(self, version):
        """
        Remove the snapshot
        """
        self.__api_client.do_delete(
            "domains/{}/snapshots/{}".format(self.__domain_id, version)
        )
