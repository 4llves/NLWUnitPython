from src.http_types.http_res import HttpRes
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpRes:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpRes(
            body = {
                "errors": [{
                    "title": error.name,
                    "details": error.message
                }]
            },
            status_code = error.status_code,
        )
    return HttpRes(
        body = {
            "errors": [{
                "title": "Deu pau! contate do dba!",
                "details": str(error),
            }]
        }
    )