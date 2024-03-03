from app.core.schemas.base import BaseResponse
from app.core.enums.response_status import ResponseStatus
from app.core.enums.status_type import StatusType


class EmbedFileSuccessfully(BaseResponse):
    status: str = StatusType.SUCCESS.value
    status_type: str = ResponseStatus.EMBED_SUCCESSFULLY.name
    message: str = ResponseStatus.EMBED_SUCCESSFULLY.message
    _status_code: int = ResponseStatus.EMBED_SUCCESSFULLY.status_code
