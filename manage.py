import http.server
import socketserver
import sys

print('argv:', sys.argv)
if len(sys.argv) < 2:
    raise Exception('need args')

cmd = sys.argv[1]

if cmd == 'migrate':
    print('fake do migrate...')
    exit()

elif cmd == 'runserver':
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('serving at port', PORT)
        httpd.serve_forever()

else:
    raise Exception('unknown cmd %s' % cmd)
