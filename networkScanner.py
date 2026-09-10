import nmap

def fit(value, width):
    """Fit a value into a fixed-width column. Prevents confusing overlapping of information spilling into other columns"""
    value = str(value or "")

    if len(value) > width:
        return value[:width - 1] + "…"

    return value.ljust(width)

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
