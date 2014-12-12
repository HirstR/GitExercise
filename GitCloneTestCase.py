import sys
import unittest
import urllib.request, http.client
import json

### SERVER_URL = "http://localhost:8000"
SERVER_URL = "https://api.github.com"

class GitCloneTestCase(unittest.TestCase):
	def setUp(self):
		self.resp = urllib.request.urlopen(SERVER_URL)

	def testResponseStatus(self):
		assert self.resp.status == http.client.OK, 'unexpected HTTP status ' + self.resp.status

	def testHeaders(self):
		assert self.resp.getheader('ETag'), 'No ETag found'

		contentType = str(self.resp.getheader('Content-Type'))
		assert contentType.startswith('application/json'), 'Wrong Content-Type header: ' + str(contentType)

		githubVersion = str(self.resp.getheader('X-GitHub-Media-Type'))
		assert githubVersion.startswith('github.v3'), 'Wrong GitHub version: ' + str(githubVersion)

		rateLimit = str(self.resp.getheader('X-RateLimit-Limit'))
		assert rateLimit == '60', 'Expected rate limit of 60 but found ' + rateLimit

		rateRemaining = str(self.resp.getheader('X-RateLimit-Remaining'))
		assert rateRemaining <= rateLimit, 'Expected smaller remaining limit'

	def testResponseBody(self):
		textBody = self.resp.read().decode('UTF-8')
		jsonBody = json.loads(textBody)

		assert 'current_user_url' in jsonBody and jsonBody['current_user_url'] == SERVER_URL + '/user', 'Unexpected current_user_url value'
		assert 'plan' not in jsonBody, 'unauthenticated user should not have plan'

if __name__ == "__main__":
	unittest.main()
