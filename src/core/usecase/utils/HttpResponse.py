class HttpResponse:

    def __init__(self, status_code: int, body: any) -> None:
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f"HttpRequest (statusCode={self.status_code}, body={self.body})"
