class GithubApiException(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP status code was: {status_code}."
        
        super().__init__("A Github API error occurred: " + message)
