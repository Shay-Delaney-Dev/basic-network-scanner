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
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])

print("\n------------------------")
