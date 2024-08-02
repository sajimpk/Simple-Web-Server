from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/sajim':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open("index.html", "rb") as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "File Not Found: index.html")
                
        elif self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open("index2.html", "rb") as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "File Not Found: index.html")
        else:
            super().do_GET()
        

PORT = 8000
with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

