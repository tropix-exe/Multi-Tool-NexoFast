import os
import platform
import subprocess

def ping():
    """Fragt nach einer IP-Adresse oder Domain und pingt diese."""
    target = input("Enter the IP or Domain to ping: ")

    
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        
        process = subprocess.run(
            ["ping", param, "4", target],  
            capture_output=True,
            text=True,
            encoding="utf-8",  
            errors="ignore"  
        )

        
        print("\n" + process.stdout)
        
    except Exception as e:
        print(f"Error while pinging {target}: {e}")

if __name__ == "__main__":
    ping()
