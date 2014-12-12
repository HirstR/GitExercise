import http.server 
import json
	
class GitClone(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.send_header('ETag', '1234567890')
		self.send_header('X-Github-Media-Type', 'github.v3; more stuff')
		self.send_header('X-RateLimit-Limit', '60')
		self.send_header('X-RateLimit-Remaining', '59')
		self.end_headers()
	
		bodytext = ('{'
			'"current_user_url": "http://localhost:8000/user",'
			'"emojis_url": "http://localhost:8000/emojis"'
		'}')
		self.wfile.write(bytes(bodytext, 'UTF-8'))

server = http.server.HTTPServer(('localhost', 8000), GitClone)
print('GitClone server starting...\n')
	
try:
	server.serve_forever()
except KeyboardInterrupt:
	pass
	
server.server_close()

print('\nGitClone server says goodbye.')
