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
# Print scan results
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())

    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)

        for port in scanner[host][proto]:
            info = scanner[host][proto][port]
            print(
                f"Port: {port:<6}",
                f"State: {info.get('state', 'unknown'):<10}",
                f"Service: {info.get('name', ''):<12}",
                f"Product: {info.get('product', ''):<20}",
                f"Version: {info.get('version', '')}"
            )

print("\n------------------------")
