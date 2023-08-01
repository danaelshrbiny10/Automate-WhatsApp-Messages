"""API App middleware."""

import logging

logger = logging.getLogger(__name__)

class LogUnhandledExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error('Unhandled exception occurred', exc_info=True)
        return None
