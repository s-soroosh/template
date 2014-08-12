import SimpleHTTPServer
import SocketServer

__author__ = 'soroosh'


PORT = 9090

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

