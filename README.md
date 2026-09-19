# Basic Network Scanner

A basic network scanner that uses Nmap to scan a target IP address, hostname, or subnet and print structured results to the terminal.

## Quick Start

1. Install the requirements:

```bash
python3 -m pip install python-nmap
```

2. Run a scan against a target

```bash
python3 networkScanner.py scanme.nmap.org 
```

## Features

- Scans an IP address, hostname, or subnet
- Detects active hosts
- Reports port states and service information
- Attempts service version and operating system detection
- Displays scan results in neatly formatted table
- Exports scan results as csv file

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

It prints the detailed table and writes the complete Nmap result to a file named
`scan_output_YYYY-MM-DD_HHMMSS.csv` in the scans directory. Extensive scans may
take longer and some Nmap options may require administrator privileges.

## Limitations

- Scan results are exported as CSV; JSON and XML reports are not supported
- The scanner is designed for learning and authorized testing only

## Responsible Use

Only scan systems and networks that you own or have explicit permission to test. Unauthorized scanning may be illegal or disruptive. The default target, `scanme.nmap.org`, is provided by Nmap for testing purposes; follow its usage policy.

## Background

I made this basic network scanner using free online resources to develop my interest in computer networking and cybersecurity.

I used these articles while developing the project:
https://medium.com/@amaltomparakkaden/automating-network-scanning-with-python-and-nmap-948948f0b161
https://labex.io/tutorials/nmap-how-to-export-nmap-scan-output-419145
https://pypi.org/project/python-nmap/
