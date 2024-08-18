from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse


def health_check(request):
    db_conn = connections["default"]
    try:
        db_conn.cursor()
        db_status = "ok"
    except OperationalError:
        db_status = "error"

    return JsonResponse(
        {
            "status": "ok" if db_status == "ok" else "error",
            "database": db_status,
        }
    )
