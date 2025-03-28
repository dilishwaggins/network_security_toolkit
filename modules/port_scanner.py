import socket
import argparse
import sys

try:
    import nmap
except ImportError:
    print("[!] Missing dependency: python-nmap. Install it with: pip install python-nmap")
    sys.exit(1)

def scan_port(target, port):
    """Attempts to connect to a target IP and port using socket."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open on {target}")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def scan_target_nmap(target, ports):
    """Scans ports using Nmap."""
    try:
        nm = nmap.PortScanner()
        port_str = ','.join(map(str, ports))
        nm.scan(target, port_str, arguments="-sS")
        
        for host in nm.all_hosts():
            print(f"Scanning {host}...")
            for port in nm[host]['tcp']:
                state = nm[host]['tcp'][port]['state']
                print(f"[+] Port {port} is {state}")
    except nmap.nmap.PortScannerError as e:
        print(f"[-] Nmap error: {e}")
    except Exception as e:
        print(f"[-] Unexpected error using Nmap: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner with Nmap Integration")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-p", "--ports", type=str, help="Comma-separated list of ports (e.g., 22,80,443)", required=True)
    parser.add_argument("--use-nmap", action="store_true", help="Use Nmap for scanning instead of socket")
    args = parser.parse_args()
    
    ports = [int(p) for p in args.ports.split(",")]
    
    if args.use_nmap:
        scan_target_nmap(args.target, ports)
    else:
        print(f"Scanning {args.target} with socket...")
        for port in ports:
            scan_port(args.target, port)
