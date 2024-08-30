import requests

req = requests.get("http://localhost:8000/hello/Tona")
print(req.json())

req = requests.get("http://localhost:8000/greet?who=Tona")
print(req.json())

req = requests.post("http://localhost:8000/greet", json={"who": "Tona"})
print(req.json())

req = requests.post("http://localhost:8000/agent", headers={"user-agent": "Mozilla/5.0"})
print(req.headers)

req = requests.get("http://localhost:8000/happy")
print(req.json())
