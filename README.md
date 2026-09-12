# Basic Network Scanner

A basic network scanner that uses Nmap to scan a target IP address, hostname, or subnet and print structured results to the terminal.

## Quick Start

1. Install the requirements:

```bash
python3 -m pip install python-nmap
```

2. Run a scan against a target:

```bash
python3 networkScanner.py scanme.nmap.org
```

This command automatically uses:
- full port scan (`-p-`)
- SYN scan (`-sS`)
- service detection (`-sV`)
- OS detection (`-O`)
- aggressive scan mode (`-A`)

## Features

- Scans an IP address, hostname, or subnet
- Detects active hosts
- Reports port states and service information
- Attempts service version and operating system detection
- Displays results in a readable table format
- Uses a single required target argument
- Automatically runs the full default Nmap scan profile

## Requirements

- Python 3
- Nmap installed on your system
- The `python-nmap` Python package

## Installation

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install nmap
python3 -m pip install python-nmap
```

### macOS

```bash
brew install nmap
python3 -m pip install python-nmap
```

### Windows

Install Nmap from the [official Nmap download page](https://nmap.org/download.html), then run:

```powershell
py -m pip install python-nmap
```

## Usage

Run the scanner from the project directory:

```bash
python3 networkScanner.py <target>
```

### Example

```bash
python3 networkScanner.py scanme.nmap.org
```

The script always runs an aggressive full-port scan using:
- `-sS`
- `-sV`
- `-O`
- `-A`
- `-p-`

This is intentionally more comprehensive than a quick scan, so it may take longer to complete. Scanning all ports and enabling service and OS detection adds extra probing and processing time. Some Nmap options may require administrator privileges.

## Limitations

- Results are printed to the terminal and are not currently saved to a file
- The script does not currently export JSON, CSV, or XML reports
- The scanner is designed for learning and authorized testing only

## Responsible Use

Only scan systems and networks that you own or have explicit permission to test. Unauthorized scanning may be illegal or disruptive. The default target, `scanme.nmap.org`, is provided by Nmap for testing purposes; follow its usage policy.

## Background

I made this basic network scanner using free online resources to develop my interest in computer networking and cybersecurity.

I used this article as one source while developing the project:
https://medium.com/@amaltomparakkaden/automating-network-scanning-with-python-and-nmap-948948f0b161
