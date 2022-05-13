from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    NotFound
)


class CustomError(HTTPException):
    pass