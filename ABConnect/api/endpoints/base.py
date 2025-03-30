class BaseEndpoint:
    _r = None

    @classmethod
    def set_request_handler(cls, handler):
        cls._r = handler
