import time
from colorama import Fore, Style, init
import requests
from banners import IP_ASCII  

def slow_print(text, delay=0.03):
    for line in text.splitlines():
        print(line)
        time.sleep(delay)

def get_ip_info(ip):
    
    slow_print(IP_ASCII)
    

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        
        print(f"\n=== {Fore.WHITE}IP-{Fore.RED}Informationen ==={Style.RESET_ALL}")
        print(f"{Fore.RED}• Land: {Fore.WHITE}{data.get('country', 'N/A')}")
        print(f"{Fore.RED}• ISP: {Fore.WHITE}{data.get('org', 'N/A')}")
        print(f"{Fore.RED}• Position: {Fore.WHITE}{data.get('loc', 'N/A')}")
    except Exception as e:
        print(f"{Fore.RED}⚠ Fehler: {e}")

if __name__ == "__main__":
    get_ip_info("8.8.8.8")  