import math
from constellixsdk.api.pool import Pool
from constellixsdk.util import CheckEmpty, param_to_json
from enum import Enum


class PoolParam():
    """
    Pool Param for Create and Update operations
    """

    class PoolItoConfig(CheckEmpty):
        """
        Pool Ito Config
        """
        class Period(Enum):
            PERIOD30 = 30
            PERIOD60 = 60
            PERIOD120 = 120
            PERIOD180 = 180
            PERIOD240 = 240
            PERIOD300 = 300

        class DeviationAllowance(Enum):
            DA10 = 10
            DA20 = 20
            DA30 = 30
            DA40 = 40
            DA50 = 50
            DA60 = 60
            DA70 = 70
            DA80 = 80
            DA90 = 90

        class MonitoringRegion(Enum):
            WORLD = "world"
            ASIAPAC = "asiapac"
            EUROPE = "europe"
            NANCENTRAL = "nacentral"
            NAEAST = "naeast"
            NAWEST = "nawest"
            OCEANIA = "oceania"
            SOUTHAMERICA = "southamerica"

        class HandicapFactor(Enum):
            NONE = "none"
            PERCENT = "percent"
            SPEED = "speed"

        def __init__(self):

            # integer : The number of seconds between each check
            self.period = None

            # integer : The maximum number of results to return
            self.maximumNumberOfResults = None

            # integer : Percentage of how much is the response time
            # allowed to deviate?
            self.deviationAllowance = None

            # string : Where monitoring should be performed from
            self.monitoringRegion = ""

            # string : Enum: "none" "percent" "speed"
            self.handicapFactor = ""
            pass

    class PoolIto(CheckEmpty):
        """
        Pool Ito
        """

        def __init__(self):

            # boolean : Is Ito enabled for this pool?
            self.enabled = None

            # The Ito configuration
            self.config = PoolParam.PoolItoConfig()

    class PoolValue(CheckEmpty):
        """
        Pool Value
        """

        class Policy(Enum):
            FOLLOW_SONAR = "follow_sonar"
            ALWAYS_OFF = "always_off"
            ALWAYS_ON = "always_on"
            OFF_ON_FAILURE = "off_on_failure"

        def __init__(self):
            # string : <ipv4> or <ipv6> or <hostname>
            self.value = ""

            # integer : A weight for the value. Must be between 1 and 1000000
            self.weight = None

            # boolean : Is this value enabled or not?
            self.enabled = None

            # integer : A handicap for this value
            self.handicap = None

            # string : The failover/check policy for this value
            self.policy = ""

            # integer : The ID of the check to use from Sonar
            self.sonarCheckId = None

    class Type(Enum):
        A = "A"
        AAAA = "AAAA"
        CNAME = "CNAME"

    def __init__(self):
        # string : The type of pool, either A, AAAA or CNAME
        self.type = ""

        # string : A name for the pool
        self.name = ""

        # integer : The minimum number of entries from the pool
        # to return when queried.
        # Between 0 and 64.
        self.returnValue = None

        # integer : The number of records that must be available
        # for this pool to be used for failover.
        # Between 0 and 64.
        self.minimumFailover = None

        # boolean : Whether the pool is enabled or not
        self.enabled = None

        # list of PoolValue : The values for this pool
        self.values = []

        # list of integers : Contact lists to be emailed
        # when this pool changes
        self.contacts = []

        # PoolIto : Pool Ito object
        self.ito = PoolParam.PoolIto()


class Pools():
    """
    Managing Pools endpoint wrapper
    """

    def __init__(self, apiclient):
        self.__api_client = apiclient

    def all(self):
        """
        Returns a list of all Pools in the account
        """
        pools = []

        currentPage = None
        while True:
            if currentPage is None:
                payload = self.__api_client.do_get("pools")
            else:
                payload = self.__api_client.do_get(
                    "pools",
                    params={"page": currentPage}
                )
            for data in payload["data"]:
                pools.append(Pool(self.__api_client, data))
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

        return pools

    def after(self, cursor):
        """
        Cursor pagination for Pool objects
        """
        pools = []

        currentPage = cursor

        if currentPage is None:
            payload = self.__api_client.do_get("pools")
        else:
            payload = self.__api_client.do_get(
                "pools",
                params={"page": currentPage}
            )

        for data in payload["data"]:
            pools.append(Pool(self.__api_client, data))

        totalPages = 1
        try:
            totalPages = payload["meta"]["pagination"]["totalPages"]
        except:
            totalPages = math.ceil(
                payload["meta"]["pagination"]["total"] /
                payload["meta"]["pagination"]["perPage"]
            )

        if payload["meta"]["pagination"]["currentPage"] >= totalPages:
            return pools, None

        cursor = payload["meta"]["pagination"]["currentPage"] + 1
        return pools, cursor

    def get_pool(self, id, poolType):
        """
        Fetches a single Pool in your account
        """
        result = self.__api_client.do_get("pools/{}/{}".format(poolType, id))
        return Pool(self.__api_client, result["data"])

    def create_pool(self, param):
        """
        Creates a new Pool in your account.
        param is PoolParam containing new Pool fields
        Returns the id of created Pool
        """

        payload = param_to_json(param)

        result = self.__api_client.do_post("pools", body=payload)
        return result["data"]["id"]
