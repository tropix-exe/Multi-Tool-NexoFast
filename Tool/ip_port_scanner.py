import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Prüft, ob ein Port auf der IP geöffnet ist."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                print(f"[✔] Port {port} is open on {ip}")
                return port
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    return None

def scan():
    """Fragt nach einer IP und scannt gängige Ports."""
    ip = input("Enter the target IP address: ")
    ports = input("Enter ports to scan (comma-separated, e.g., 22,80,443): ")
    port_list = [int(p.strip()) for p in ports.split(",")]

    print(f"\nScanning {ip} on {len(port_list)} ports...\n")
    open_ports = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in port_list]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)

    print("\nScan complete!")
    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
