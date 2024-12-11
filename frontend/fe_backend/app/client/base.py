import httpx
from typing import Any, Dict, Optional


class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url)

    def _handle_response(self, response: httpx.Response) -> Any:
        if response.status_code >= 400:
            response.raise_for_status()
        return response.json()

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        response = self.client.get(endpoint, params=params)
        return self._handle_response(response)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]]) -> Any:
        response = self.client.post(endpoint, json=data)
        return self._handle_response(response)

    def delete(self, endpoint: str) -> Any:
        response = self.client.delete(endpoint)
        return self._handle_response(response)

    def close(self):
        self.client.close()
