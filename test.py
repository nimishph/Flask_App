import repos.api
import repos.exceptions
import unittest

class TestCreateQuery(unittest.TestCase):
    def test_create_query(self):
        test_languages = ['Python', 'JavaScript',' Java']
        test_min_stars = 10000
        
        expected = "language:Python language:JavaScript language:Java stars:>10000"
        
        self.assertEqual(result, expected, "Unexpeccted result from create_query")
    
class TestGitHubApiException(unittest.TestCase):
    def test_exception_403(self):
        status_code = 403
        exception = repos.exception.GithubApiException(status_code)
        
        self.assertTrue("Rate limit" in str(exception), "'Rate limit' not found")
    
    def test_exception_500(self):
        status_code  = 500
        exception = repos.exception.GithubApiException(status_code)
        
        self.assertTrue(str(status_code) in str(exception))
         
if __name__ == '__main__':
    unittest.main()