class ConstellixApiError(Exception):
    """
    API error
    """

    def __init__(self, message=None, response=None, exception=None):
        if message is not None:
            self.__message = message
        if exception is not None:
            self.__exception = exception

    @property
    def message(self):
        try:
            return self.__message
        except AttributeError:
            return None

    @property
    def exception(self):
        try:
            return self.__exception
        except AttributeError:
            return None


class RequestLimitExceeded(ConstellixApiError):
    pass


class NotAuthorized(ConstellixApiError):
    pass


class RequestCouldNotBeProcessed(ConstellixApiError):
    pass
