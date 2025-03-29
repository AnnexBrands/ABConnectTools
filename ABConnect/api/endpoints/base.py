class BaseEndpoint:
    def __init__(self, request_handler):
        self._r = request_handler