import http.server
import socketserver
import os

def serve(PORT = 8000, directory = "./"):
    os.chdir(directory)
    
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.extensions_map.update({
        '.webapp': 'application/x-web-app-manifest+json',
    })
    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("Serving at port", PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    serve()
