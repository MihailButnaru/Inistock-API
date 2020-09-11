from rest_framework import status
from rest_framework.exceptions import APIException


class PersonNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "bad_request"


class ShareNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "bad_request"


class PersonIDNotValid(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "bad_request"
