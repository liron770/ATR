from __future__ import annotations
import io
from typing import Iterable
import pytest
import requests
import time
from config import *

def _url(path: str) -> str:
    return f"{BASE_URL}{path}"

def assert_status_in(response: requests.Response, allowed: Iterable[int]) -> None:
    allowed_set = set(allowed)
    assert response.status_code in allowed_set, (
        f"{response.request.method} {response.url} -> {response.status_code}, "
        f"body={response.text[:500]!r}; allowed={sorted(allowed_set)}"
    )

def assert_json_if_ok(response: requests.Response) -> None:
    if response.headers.get("content-type", "").split(";")[0].strip() == "application/json":
        response.json()

def assertion_Get(apiUrl, params=None, instanceType=None, responseCodes=(200,), isJson=True) -> None:
        r = SESSION.get(_url(apiUrl), params=params)
        assert_status_in(r, responseCodes)
        if(instanceType!=None):
            assert isinstance(r.json(), instanceType)
        if(isJson):
            assert_json_if_ok(r)

def assertion_Post(apiUrl,json=None, responseCodes=(200,)) -> None:
        r = SESSION.post(_url(apiUrl), json=json)
        print("STATUS:", r.status_code)
        print("BODY:", r.text)
        assert_status_in(r, responseCodes)
        assert_json_if_ok(r)
def restartNeuronicServer(apiUrl) -> None:
        try:
            SESSION.post(_url(apiUrl))
        except requests.exceptions.ConnectionError:
            pass  
        time.sleep(5)
        assertion_Get("/api/getProfiles")
def selectedFiles(apiUrl) -> None:
    files = {
        "file1": ("vis_d.onnx", io.BytesIO(b"\x80placeholder"), "application/octet-stream"),
        "file3": ("vis_c.onnx", io.BytesIO(b"\x80placeholder"), "application/octet-stream"),
        "file4": ("vis.yaml", io.BytesIO(b"names:\n  - car\n"), "application/x-yaml"),
    }
    data = {"size": "640"}
    r = SESSION.post(_url(apiUrl), files=files, data=data)
    assert_status_in(r, (200,))
    assert_json_if_ok(r)
