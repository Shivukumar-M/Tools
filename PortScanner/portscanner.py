import socket
import threading

print_lock = threading.Lock()

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ipaddress, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port Open: {port}")
        else:
            with print_lock:
                print(f"[-] Port Closed: {port}")
        sock.close()
    except Exception as e:
        with print_lock:
            print(f"[!] Error on port {port}: {e}")


def scan(target, ports):
    print(f"\n[*] Starting Scan for {target}")
    threads = []
    for port in range(1, ports + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

targets = input("[*] Enter the targets to scan (split with ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets:")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)
