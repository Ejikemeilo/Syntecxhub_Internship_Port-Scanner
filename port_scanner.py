import socket
import threading
from datetime import datetime

def scan_port(host, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"  [OPEN]   Port {port}")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        pass  # Ignore errors silently

def run_scanner(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}")
    print(f"Started at: {datetime.now()}\n")
    
    open_ports = []
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nScan complete.")
    print(f"Open ports found: {sorted(open_ports)}")
    print(f"Finished at: {datetime.now()}")

# Main
host  = input("Enter host (e.g. 127.0.0.1): ")
start = int(input("Start port: "))
end   = int(input("End port: "))

run_scanner(host, start, end)