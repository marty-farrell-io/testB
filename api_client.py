
import requests

class APIClient:
    def __init__(self, base_url="http://api.example.com/v1", api_key=None):
        self.base_url = base_url
        self.api_key = api_key

    
    
    def (self, **params):
        url = self.base_url + "/users"
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params.get('query'), json=params.get('body'))
        return self.handle_response(response)

    
    
    
    def (self, **params):
        url = self.base_url + "/users/{userId}"
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params.get('query'), json=params.get('body'))
        return self.handle_response(response)

    
    

    def get_headers(self):
        headers = {}
        if self.api_key:
            headers['Authorization'] = f"Bearer {self.api_key}"
        return headers

    def handle_response(self, response):
        if response.status_code != 200:
            raise Exception(f"API request failed with status {response.status_code} and message: {response.text}")
        return response.json()

# Example usage:
# client = APIClient(api_key='your_api_key')
# response = client.some_endpoint(method='GET', params={'query': {'key':'value'}})