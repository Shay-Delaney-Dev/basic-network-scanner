import nmap

# Create new scanner object
scanner = nmap.PortScanner()

# Define target IP address/hostname
target = "scanme.nmap.org"

# Define nmap options
options = "-sS -sV -O -A -p 1-1000"

# Run basic scan on target with specified options
scanner.scan(target, arguments=options)

print("\n----- Scan Results -----\n")

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}\n")

    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto.upper()}")

        # Table header
        print(
            f"{'PORT':<8}"
            f"{'STATE':<10}"
            f"{'REASON':<12}"
            f"{'SERVICE':<15}"
            f"{'PRODUCT':<22}"
            f"{'VERSION':<15}"
            f"{'EXTRA INFO':<25}"
        )

        print("-" * 107)

        for port in sorted(scanner[host][proto]):
            info = scanner[host][proto][port]

            print(
                f"{port:<8}"
                f"{info.get('state', ''):<10}"
                f"{info.get('reason', ''):<12}"
                f"{info.get('name', ''):<15}"
                f"{info.get('product', ''):<22}"
                f"{info.get('version', ''):<15}"
                f"{info.get('extrainfo', ''):<25}"
            )

        print()

print("------------------------")
