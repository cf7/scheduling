class Endpoint:

    def __init__(self, url: str, handler: callable):
        self.url = url
        self.handler = handler


class Request:

    def __init__(self, protocol: str):
        self.protocol = protocol


endpoint_factory = {
}