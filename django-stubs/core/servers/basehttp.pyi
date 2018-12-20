import socketserver
from io import BytesIO
from typing import Any, Dict
from wsgiref import simple_server

from django.core.handlers.wsgi import WSGIRequest

class WSGIServer(simple_server.WSGIServer):
    request_queue_size: int = ...
    address_family: Any = ...
    allow_reuse_address: Any = ...
    def __init__(self, *args: Any, ipv6: bool = ..., allow_reuse_address: bool = ..., **kwargs: Any) -> None: ...
    def handle_error(self, request: Any, client_address: Any) -> None: ...

class ThreadedWSGIServer(socketserver.ThreadingMixIn, WSGIServer): ...

class ServerHandler(simple_server.ServerHandler):
    http_version: str = ...
    def handle_error(self) -> None: ...

class WSGIRequestHandler(simple_server.WSGIRequestHandler):
    client_address: str
    close_connection: bool
    connection: WSGIRequest
    request: WSGIRequest
    rfile: BytesIO
    server: None
    wfile: socketserver._SocketWriter
    protocol_version: str = ...
    def address_string(self) -> str: ...
    def log_message(self, format: str, *args: Any) -> None: ...
    def get_environ(self) -> Dict[str, str]: ...
    raw_requestline: bytes = ...
    requestline: str = ...
    request_version: str = ...
    command: None = ...
    def handle(self) -> None: ...