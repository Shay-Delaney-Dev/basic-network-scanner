import argparse
import nmap
from datetime import datetime
from pathlib import Path

def fit(value, width):
    """Helper method to fit a value into a fixed-width column. Prevents confusing overlapping of information spilling into other columns."""
    value = str(value or "")

    if len(value) > width:
        return value[:width - 1] + "…"

    return value.ljust(width)

def run_scan(target):
    """Runs nmap scan on target IP address/hostname."""
    scanner = nmap.PortScanner()
    scanner.scan(target)
    return scanner

def print_scan(scanner):
    """Prints scan results to console in a neatly formatted table."""
    print("\n----- Scan Results -----\n")

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}\n")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto.upper()}")
            print(
                fit("PORT", 8),
                fit("STATE", 10),
                fit("REASON", 12),
                fit("SERVICE", 15),
                fit("PRODUCT", 20),
                fit("VERSION", 20),
                fit("EXTRA INFO", 30)
            )
            print("-" * 127)
            for port in sorted(scanner[host][proto]):
                info = scanner[host][proto][port]
                print(
                    fit(port, 8),
                    fit(info.get("state"), 10),
                    fit(info.get("reason"), 12),
                    fit(info.get("name"), 15),
                    fit(info.get("product"), 20),
                    fit(info.get("version"), 20),
                    fit(info.get("extrainfo"), 30)
                )
            print()

    print("------------------------")

def to_file(scanner):
    """Saves scans to csv files in scans directory."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    folderPath = Path("scans")
    filename = f"scan_output_{timestamp}.csv"

    folderPath.mkdir(parents=True, exist_ok=True)

    filePath = folderPath / filename
    with open(filePath, 'w') as f:
        f.write(scanner.csv())

def get_target():
    """Get and return target input from user."""
    parser = argparse.ArgumentParser(description="Network scanner using Nmap.")
    parser.add_argument("target", help="Target IP, hostname, or subnet to scan")
    args = parser.parse_args()
    return args.target

def main():
    target = get_target()
    scanner = run_scan(target)
    to_file(scanner)
    print_scan(scanner)

if __name__ == "__main__":
    main()