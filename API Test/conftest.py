import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("GEOALGTR_API_BASE", "http://192.168.1.10:8000").rstrip("/")


@pytest.fixture(scope="session")
def api_session(base_url: str):
    import requests

    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    s.base_url = base_url  # type: ignore[attr-defined]
    return s


@pytest.fixture(scope="session", autouse=True)
def _require_api_reachable(api_session):
    import requests

    try:
        api_session.get(f"{api_session.base_url}/api/getNic", timeout=3)
    except requests.RequestException as exc:
        pytest.skip(f"GeoAlgtr API not reachable at {api_session.base_url}: {exc}")
