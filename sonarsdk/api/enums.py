from enum import Enum


class VerificationPolicy(Enum):
    SIMPLE   = "SIMPLE"
    MAJORITY = "MAJORITY"


class ProtocolType(Enum):
    HTTP    = "HTTP"
    HTTPS   = "HTTPS"
    TCP     = "TCP"
    UDP     = "UDP"
    DNS     = "DNS"
    RUM     = "RUM"
    ICMP    = "ICMP"


class RecordType(Enum):
    AAAA    = "AAAA"
    A       = "A"
    ANAME   = "ANAME"
    CAA     = "CAA"
    CERT    = "CERT"
    CNAME   = "CNAME"
    HINFO   = "HINFO"
    HTTP    = "HTTP"
    MX      = "MX"
    NAPTR   = "NAPTR"
    NS      = "NS"
    PTR     = "PTR"
    RP      = "RP"
    SPF     = "SPF"
    SRV     = "SRV"
    TXT     = "TXT"


class CompareOption(Enum):
    EQUALS      = "EQUALS"
    CONTAINS    = "CONTAINS"
    ONEOFF      = "ONEOFF"
    ANYMATCH    = "ANYMATCH"


class MonitorIntervalPolicy(Enum):
    PARALLEL        = "PARALLEL"
    ONCEPERSITE     = "ONCEPERSITE"
    ONCEPERREGION   = "ONCEPERREGION"


class MonitorInterval(Enum):
    FIVESECONDS     = "FIVESECONDS"
    THIRTYSECONDS   = "THIRTYSECONDS"
    ONEMINUTE       = "ONEMINUTE"
    TWOMINUTES      = "TWOMINUTES"
    THREEMINUTES    = "THREEMINUTES"
    FOURMINUTES     = "FOURMINUTES"
    FIVEMINUTES     = "FIVEMINUTES"
    TENMINUTES      = "TENMINUTES"
    THIRTYMINUTES   = "THIRTYMINUTES"
    HALFDAY         = "HALFDAY"
    DAY             = "DAY"


class DNSCompareOption(Enum):
    EQUALS      = "EQUALS"
    CONTAINS    = "CONTAINS"
    ONEOFF      = "ONEOFF"
    ANYMATCH    = "ANYMATCH"


class DNSQueryProtocol(Enum):
    TCP = "TCP"
    UDP = "UDP"


class IPVersion(Enum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class ScheduleInterval(Enum):
    NONE    = "NONE"
    DAILY   = "DAILY"
    WEEKLY  = "WEEKLY"
    MONTHLY = "MONTHLY"


class RunTraceroute(Enum):
    DISABLED            = "DISABLED"
    ON_STATUS_CHANGE    = "ON_STATUS_CHANGE"
    WITH_CHECK          = "WITH_CHECK"
