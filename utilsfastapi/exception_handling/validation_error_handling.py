from fastapi import (
    FastAPI,
    Request,
    status,
    Response,
)
from orjson import dumps
from fastapi.exceptions import RequestValidationError


HTTP_422_UNPROCESSABLE_ENTITY = status.HTTP_422_UNPROCESSABLE_ENTITY


def prepare_handler_for_validation_errors_function(
    fast_api_app: FastAPI,
):

    async def handler_for_validation_error(
        request: Request,
        exc: RequestValidationError,
    ) -> Response:
        exe_error = exc.errors()
        return Response(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content=dumps(
                {
                    "status_code": HTTP_422_UNPROCESSABLE_ENTITY,
                    "success": False,
                    "data": None,
                    "error": exe_error,
                }
            ),
            media_type="application/json",
        )

    fast_api_app.exception_handler(RequestValidationError)(handler_for_validation_error)
