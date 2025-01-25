from traceback import format_exc
from logging import Logger

from fastapi import (
    Request,
    FastAPI,
    Response,
)
from orjson import dumps
from utilsfastapi.settings import EnumRunMode

from .project_base_exception import ProjectBaseException

from .create_traceback import create_traceback


def prepare_handler_for_project_base_exception_function(
        fast_api_app: FastAPI,
        logger: Logger,
        run_mode: EnumRunMode,
):
    async def handler_for_project_base_exception(
            request: Request,
            exc: ProjectBaseException
    ) -> Response:
        status_code = getattr(exc,"status_code", 500)
        success = getattr(exc,"success", None)
        data = getattr(exc,"data", None)
        error = getattr(exc,"error", None)
        
        if status_code >= 500:
            traceback_ = None
            if getattr(
                    exc,
                    "log_this_exc",
                    True,
            ):
                traceback_ = await create_traceback(
                    exc=exc,
                    request=request,
                    traceback_=format_exc(),
                )
                logger.error(msg=traceback_)

            status_code = status_code
            success = False
            data = None

            if run_mode == EnumRunMode.PRODUCTION:
                error = error
            else:
                error = f"{error}\n{traceback_}" if traceback_ else error

        return Response(
                    status_code=status_code,
                    content=dumps(
                        {
                            "status_code": status_code,
                            "success": success,
                            "data": data,
                            "error": error,
                        }
                    ),
                    media_type="application/json",
                )


    fast_api_app.exception_handler(ProjectBaseException)(handler_for_project_base_exception)
