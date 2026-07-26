"""Integration tests for rate limit headers on responses.
Requires the app running locally (make run) and Docker services up.
"""

import httpx
import pytest

BASE_URL = "http://localhost:8000"


@pytest.fixture
def client() -> httpx.Client:
    return httpx.Client(base_url=BASE_URL)


class TestRateLimitHeaders:
    def test_response_includes_rate_limit_headers(self, client: httpx.Client) -> None:
        response = client.get("/")

        assert response.status_code == 200
        assert "X-RateLimit-Limit" in response.headers
        assert "X-RateLimit-Remaining" in response.headers
