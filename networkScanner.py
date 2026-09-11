import nmap

def fit(value, width):
    """Helper method to fit a value into a fixed-width column. Prevents confusing overlapping of information spilling into other columns."""
    value = str(value or "")

    if len(value) > width:
        return value[:width - 1] + "…"

    return value.ljust(width)

def run_scan(target, options):
    """Runs nmap scan on target IP address/hostname using specified options."""
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments=options)
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
                fit("EXTRA INF0", 30)
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

def main():
    target = "scanme.nmap.org"
    # Define scan options
    options = "-sS -sV -O -A -p 1-1000"
    scanner = run_scan(target, options)
    print_scan(scanner)

if __name__ == "__main__":
    main()