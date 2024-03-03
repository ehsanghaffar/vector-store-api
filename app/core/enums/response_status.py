from http import HTTPStatus
from enum import Enum


class ResponseStatus(Enum):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    EMBED_SUCCESSFULLY = (HTTPStatus.OK, 'Embed successfully')
    EMBED_FAILED = (HTTPStatus.BAD_REQUEST, 'Embed failed')
    EMBED_NOT_FOUND = (HTTPStatus.NOT_FOUND, 'Embed not found')
    EMBED_ALREADY_EXISTS = (HTTPStatus.CONFLICT, 'Embed already exists')
    EMBED_DELETED = (HTTPStatus.OK, 'Embed deleted')
