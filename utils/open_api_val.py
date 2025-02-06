import requests
import json
from openapi_spec_validator import validate

BASE_URL = "http://www.hypotheticalWalletAPI/swagger.json"
HEADERS = {"Content-Type": "application/json"}

response = requests.get(BASE_URL)
print(response.text)


class WalletAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers.copy()

    def set_auth_token(self, token):
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def load_openapi_spec(self, spec_path="swagger.json"):
        with open(spec_path, "r") as spec_file:
            spec = json.load(spec_file)
        validate(spec)
        print(spec)

    def get_endpoint(self, spec, endpoint_name, method):
        paths = spec.get("paths", {})
        for path, methods in paths.items():
            if method.lower() in methods and endpoint_name in path:
                return path
        return None

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return requests.request(method, url, headers=self.headers, **kwargs)
