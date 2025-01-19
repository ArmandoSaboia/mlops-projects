import requests
from typing import Dict

class IPValidator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.ipstack.com"

    def validate_ip(self, ip_address: str) -> Dict:
        """Validate IP address and get location details."""
        url = f"{self.base_url}/{ip_address}?access_key={self.api_key}"
        response = requests.get(url)
        return response.json() 