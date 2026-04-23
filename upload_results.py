import json
import requests

with open("report.json") as f:
    data = json.load(f)

rows = []

for test in data["tests"]:
    name = test["nodeid"].split("::")[-1]
    status = test["outcome"]
    duration = test.get("call", {}).get("duration")
    error = ""
    if status == "failed":
        error = test.get("call", {}).get("crash", {}).get("message", "")

    rows.append({
        "test_name": name,
        "status": status,
        "duration": duration,
        "error": error
    })

payload = {
    "header": ["test_name", "status", "duration", "error"],
    "rows": rows
}

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzHpelhXIdL4vmr7SsfMHEvpXxlMUCHizqJCI98lJRp-CYvNlf7KXEi5QPyblktDi7DoQ/exec"

response = requests.post(
    WEBHOOK_URL,
    data=json.dumps(payload),              
    headers={"Content-Type": "application/json"},  
    allow_redirects=True                  
)

print(response.text)