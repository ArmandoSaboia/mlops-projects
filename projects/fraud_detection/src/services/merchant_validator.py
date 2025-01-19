import requests
from typing import Dict

class MerchantValidator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://logo.clearbit.com"

    def get_merchant_data(self, domain: str) -> Dict:
        """Get merchant logo and company data."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.base_url}/{domain}"
        response = requests.get(url, headers=headers)
        return response.json() 