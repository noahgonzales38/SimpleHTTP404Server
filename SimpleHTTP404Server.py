import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class SimpleHTTP404RequestHandler(SimpleHTTPRequestHandler):
    """
    Overrides the default request handler to handle custom 404 pages as 404.html
    (i.e. a 404.html page located in the root). This behavior is seen on:
        GitHub:     https://help.github.com/articles/custom-404-pages/
        FastMail:   https://www.fastmail.com/help/files/website.html
    """
    def do_GET(self):
        path = self.translate_path(self.path)

        # If the path doesn't exist, fake it to be the 404 page.
        if not os.path.exists(path):
            self.path = '404.html'

        # Call the superclass methods to actually serve the page.
        super().do_GET()


if __name__ == '__main__':
    # Create the HTTP server on a specific address and port
    server_address = ('', 8000)  # Serve on all available interfaces on port 8000
    httpd = HTTPServer(server_address, SimpleHTTP404RequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
