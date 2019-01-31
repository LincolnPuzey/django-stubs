from typing import Type

from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SessionMiddleware(MiddlewareMixin):
    SessionStore: Type[SessionBase] = ...
    def process_request(self, request: WSGIRequest) -> None: ...
    def process_response(self, request: WSGIRequest, response: HttpResponse) -> HttpResponse: ...
