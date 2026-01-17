import pytest
import requests

@pytest.mark.api
def test_api_smoke():
    r = requests.get("https://httpbin.org/get", timeout=10)
    if r.status_code in (401, 403):
        pytest.skip("Blocked by network")
    assert r.status_code == 200
