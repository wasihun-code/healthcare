from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exceptions_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_resp = {
            'error': response.data,
        }

        return Response(custom_resp, status=response.status_code)

    return Response({
        'error': 'Internal Server Error. Please try again later.',
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)