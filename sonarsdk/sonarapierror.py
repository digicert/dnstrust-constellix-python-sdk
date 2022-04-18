class SonarApiError(Exception):
    """
    General Sonar API error
    """

    def __init__(self, message=None, exception=None):
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


class RequestLimitExceeded(SonarApiError):
    pass


class NotAuthorized(SonarApiError):
    pass


class RequestCouldNotBeProcessed(SonarApiError):
    pass
