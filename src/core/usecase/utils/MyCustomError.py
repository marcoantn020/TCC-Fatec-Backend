class MyCustomError(Exception):

    def __init__(self, message: str = None, status_code: int = 400) -> None:
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return str(self.message)
