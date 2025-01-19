import requests
from typing import Dict

class CompanyValidator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.orb-intelligence.com/v1"

    def verify_company(self, company_name: str) -> Dict:
        """Verify company information."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.base_url}/search?q={company_name}"
        response = requests.get(url, headers=headers)
        return response.json() 