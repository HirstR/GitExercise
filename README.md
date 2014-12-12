GitExercise
===========

Exercise the GitHub developer API

My immediate concern in testing this API is that the specification is very large and detailed, with many tightly interlocking parts developed somewhat organically over time.  It was not necessarily developed with any expectation that individual pieces could function independently of the whole.  Moreover, while this admittedly a hypothetical exercise, any real-world attempt to "clone" the functionality of a service as popular and well-regarded as GitHub would have to meet a very high bar in terms of reliability, stability and ease of operation.  Any partial or less-than-flawless rollout of a re-implementation would seem to be a recipe for failure. Nevertheless, fools rush in where angels fear to tread, so if I were indeed tasked with this project I would need to identify those parts of the specification that can be implemented and tested without dependencies on other parts of the specification. 

I would start with the Root Endpoint (e.g. http://api.github-clone.com/, or just http://localhost:8000 in my stub implementation.)  This has a number of advantages:
<ol>
<li>Accessing this endpoint does not require authentication (which would be the next part to be tested.)</li>
<li>Accessing this endpoint does not require that any repositories exist yet (creating repositories would be the 3rd area to target for testing.)</li>
<li>This endpoint can serve as a semi-formal handoff from the developers; the test automation would validate that a limited, fixed set of URLs would be returned.  The developers would then agree to only add a category endpoint URL to the list returned by the Root Endpoint once that particular endpoint is ready to test to some degree.  This would then trigger a failure of the test automation as a signal to the test team that a new suite of tests needs be added.</li>
</ol>

Ideally the test team would already be prepared to provide automated test suites.  This is one of the rare cases where the entire test coverage should be fully automated, because an extensive, robust, unambiguous and fully approved specification already exists.  (Needless to say, this rarely exists in any real-world case; normally, manual exploratory testing is necessary to clarify ambiguous or missing areas of the specification.)  

Another reason to push for full, extensive automation would be to ensure the expected level of reliability and stability as alluded to in the first paragraph above.

An implementation of a client test stub is included in this repository.  I chose Python to implement the tests, since the language is designed to be easy to read and maintain, including inline documentation.  Also, there is broad developer and tool support, including bindings to test libraries such as Selenium.  There are even several GitHub client implementations, such as PyGitHub, which would serve as excellent interoperability acid tests for this ersatz GitHub implementation.

A very basic stub test server is also included.  It simply serves the same static HTTP response regardless of input.


INSTRUCTIONS:
<ol>
<li>Python 3.x must be installed.</li>
<li>Download GitCloneStub.py and GitCloneTestCase.py from this repository.</li>
<li>In a terminal window, start the stub test server with 'python3 GitCloneStub.py'.<br />
   You should see the message 'GitClone server starting'.</li>
<li>In a separate terminal window, start the test client with 'python3 GitCloneTestCase.py'.<br />
   You should see output similar to
   <pre>
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.123s

   OK
   </pre></li>

<li>Stop the stub test server by pressing Ctrl-C in the first terminal window.</li>
<li>If you're feeling more adventurous, you can change the SERVER_URL value in GitCloneTestCase.py from
     'http://localhost:8000' 
    to
     'https://api.github.com'
  and rerun the tests against the actual GitHub server.  The tests should pass as before.
</li>
</ol>
