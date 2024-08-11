from rest_framework import status
from rest_framework.exceptions import APIException


class NoFileProvidedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "No file provided."
    default_code = "no_file_provided"
