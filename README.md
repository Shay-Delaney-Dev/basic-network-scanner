# Basic Network Scanner

A basic Python network scanner that uses Nmap to scan a target IP address, hostname, or subnet and print the results in a table.

## Features

- Scans an IP address, hostname, or subnet
- Detects active hosts
- Reports port states and service information
- Attempts service version and operating system detection
- Displays results in the terminal

## Requirements

- Python 3
- Nmap
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

Install Nmap from [the official Nmap download page](https://nmap.org/download.html), then run:

```powershell
py -m pip install python-nmap
```

## Usage

Run the scanner from the project directory:

```bash
python3 networkScanner.py
```

The default target is `scanme.nmap.org`. To scan another authorized target, change the `target` value in `main()`:

The scan requests service/version detection, operating system detection, additional information, and ports 1-1000. Some Nmap scan options may require administrator privileges.

## Limitations

- Results are printed to the terminal and are not currently saved to a file.
- The target is configured in the source code rather than entered at runtime.
- The scanner does not currently export JSON or CSV reports.

## Responsible Use

Only scan systems and networks that you own or have explicit permission to test. Unauthorized scanning may be illegal or disruptive. The default target, `scanme.nmap.org`, is provided by Nmap for testing purposes; follow its usage policy.

## Background

I made this basic network scanner using free online resources to develop my interest in computer networking and cybersecurity.

I used this article as one source while developing the project:
https://medium.com/@amaltomparakkaden/automating-network-scanning-with-python-and-nmap-948948f0b161
