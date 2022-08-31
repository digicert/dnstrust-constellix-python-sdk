import json
from json import JSONEncoder
from enum import Enum
# import re

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.
    Usage::
        >>> util.join_url("example.com", "index.html")
        'example.com/index.html'
    """
    for path in paths:
        url += path  # re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def join_url_params(url, params):
    """Constructs percent-encoded query string from given parms dictionary
     and appends to given url
    Usage::
        >>> util.join_url_params(
            "example.com/index.html",
            {"page": 2, "perpage": "50"}
        )
        example.com/index.html?page=2&perpage=50
    """
    return url + "?" + urlencode(params)


def parse_payload(payload, name):
    if not payload:
        return None

    return (
        payload[name]
        if name in payload
        else None
    )


class CheckEmpty():
    pass


def remove_empty_elements(d):
    """
    recursively remove empty lists, empty dicts,
    or None elements from a dictionary
    """

    def empty(x):
        if isinstance(x, CheckEmpty):
            if remove_empty_elements(x.__dict__) == {}:
                return True
        return x is None or x == "" or x == {} or x == []

    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return [
            v for v in (remove_empty_elements(v) for v in d)
            if not empty(v)
        ]
    else:
        return {
            k: v for k, v in ((k, remove_empty_elements(v)) for k, v in d.items()) if (not empty(v) or k == "name")
        }


class ParamEncoder(JSONEncoder):
    def default(self, o):
        # encoding enums
        if isinstance(o, Enum):
            return o.value

        # remove empty fields
        d = remove_empty_elements(o.__dict__)

        # replace returnValue with return
        value = d.pop("returnValue", None)
        if value is not None:
            d["return"] = value
        return d


def param_to_json(param):
    return json.dumps(param, cls=ParamEncoder)

