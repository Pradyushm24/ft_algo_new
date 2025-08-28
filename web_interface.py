import logging
import threading
import http.server
import json
import socketserver

logger = logging.getLogger(__name__)

class WebInterface:
    """Provides a simple web interface to view bot status."""

    def __init__(self, trading_bot, config: Dict[str, Any]):
        self.trading_bot = trading_bot
        self.port = config.get('port', 8000)

    def run(self):
        """Starts the web server."""
        Handler = SimpleWebHandler
        Handler.trading_bot = self.trading_bot

        with socketserver.TCPServer(("", self.port), Handler) as httpd:
            logger.info(f"Serving bot status at http://localhost:{self.port}")
            httpd.serve_forever()

class SimpleWebHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve bot status."""

    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = self.trading_bot.get_status()
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found. Use /status to get bot status.")
