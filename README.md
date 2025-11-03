# COMRADE ENDPOINTS FINDER

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A terminal-based tool to discover hidden endpoints and URLs on a target website. Designed for penetration testers, security enthusiasts, and web developers to quickly find admin panels, API endpoints, login pages, and more.

---

## Features

- Automatically fetches all links from a target website.
- Brute-forces common endpoints using a built-in wordlist.
- Supports command-line arguments for easy use.
- Colored output for better readability.

---

## Installation

### Using GitHub

```bash
# Clone the repository
git clone https://github.com/Comrade-P/Comrade-EndPoints-Finder.git
cd Comrade-EndPoints-Finder

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install the package
pip install -e .

After installation, you can run the tool from anywhere in the terminal:-

# Usage(How To Run)
comrade_endpoints https://example.com
