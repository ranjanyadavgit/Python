import requests
from requests.auth import HTTPBasicAuth
import json
url = "https://ranjanyadav19961925.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0DARycNHYYY7Bar8F95y1u9dQxGqrhm2oKvYUKeWVG4St0SgzluaslB-3OBjbKYO1l1QR1tenfEFsXu4pA48bE7Fby-K0dK6HkG8vOQOPj9O5omqtxD5JpO1Lnl01CNGjH-n29jiU76KqMUO0a0DQVCb3dI0seWb_kUxSEKNpsao=1E13D1B7"
HTTPBasicAuth("ranjanyadav19961925@gmail.com",API_TOKEN)

headers = {
  "Accept": "application/json"

}

response = requests.request(
  "GET",
  url,
  headers=headers,
  auth=auth,
)

output = json.loads(response.text)
name = output[0]["name"]
print("name is :",name)

Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-14/exampples (main)
$ python list_projects.py 
name is: My Kanban Project
