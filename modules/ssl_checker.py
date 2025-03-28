#!/usr/bin/env python3

import socket
import ssl
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="ssl_checker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_ssl_expiry(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.utcnow()).days
                print(f"✅ SSL certificate for {domain} expires on {expire_date} ({days_left} days left)")
                logging.info(f"Checked {domain} | Expires on: {expire_date} | {days_left} days left")
    except Exception as e:
        print(f"❌ Failed to check SSL certificate for {domain}: {e}")
        logging.error(f"Error checking {domain}: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain to check (without https://): ").strip()
    check_ssl_expiry(domain)
