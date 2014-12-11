GitExercise
===========

Exercise the GitHub developer API

My immediate concern in testing this API is that the specification is very large and detailed, with many tightly interlocking parts developed somewhat organically over time.  It was not necessarily developed with any expectation that any individual pieces could function independently of the whole.  Moreover, while this admittedly a hypothetical exercise, any real-world attempt to "clone" the functionality of a service as popular and well-regarded as GitHub would have to meet a very high bar for in terms of reliability, stability and ease of operation.  Any partial or less-than-flawless rollout of a re-implementation would seem to be a recipe for failure.  Nevertheless, fools rush in where angels fear to tread, so if I were indeed tasked with this project I would need to identify those parts of the specification that can be implemented and tested without dependencies on other parts of the specification. 

Thus, I would start with the Root Endpoint (e.g. http://api.github-clone.com/, or just http://localhost:8000 in my stub implementation.)  
This has a number of advantages:
<ol>
<li>Accessing this endpoint does not require authentication (which would be the next part to be tested.)</li>
<li>Accessing this endpoint does not require that any repositories exist yet (creating repositories would be the 3rd area to target for testing.)</li>
<li>This endpoint can serve as a semi-formal handoff from the developers; the test automation would validate that a limited, fixed set of URLs would be returned.  The developers would then agree to only add a category endpoint URL to the list returned by the Root Endpoint once that particular endpoint is ready to test to some degree.  This would then trigger a failure of the test automation as a signal to the test team that a new suite of tests needs be added.</li>
</ol>

Ideally the test team would already be prepared with the test suites; this is one of the rare cases where the entire test coverage should be fully automated, because an extensive, robust, unambiguous and fully approved specification already exists.  (Needless to say, this rarely exists in any real-world case; normally, manual exploratory testing is necessary to clarify ambiguous or missing areas of the specification.)  

Another reason to push for full, extensive automation would necessary to ensure the level of reliability and stability alluded to in the first paragraph above.

An implementation of a test stub is included in this repository.  I chose Python to implement the tests, since the language is designed to be easy to read and maintain, including inline documentation.  Also, there is broad developer and tool support, including bindings to test libraries such as Selenium.  There are even several GitHub client implementations, such as PyGitHub, which would serve as excellent interoperability acid tests for this ersatz GitHub implementation.

