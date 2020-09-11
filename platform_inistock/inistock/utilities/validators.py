"""Validators of the project"""
from django.core.handlers.wsgi import WSGIRequest

from inistock.exceptions.api_exceptions import PersonIDNotValid


def get_person_id(request: WSGIRequest) -> int:
    person_id = request.headers.get("PERSON-ID")

    if not person_id:
        raise PersonIDNotValid(
            detail=f"[PERSON-ID] header is missing while doing a {request.method} request"
        )

    return person_id
