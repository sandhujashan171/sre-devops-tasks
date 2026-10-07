#!/usr/bin/env python3
import urllib.request
import os
import urllib.error

TARGET_URL = os.getenv("CHECK_URL", "[https://www.google.com](https://www.google.com)")

def check_health():
    print(f"Checking health for {TARGET_URL}...")
    try:
        # Attempt to open the URL
        response = urllib.request.urlopen(TARGET_URL)
        if response.getcode() == 200:
            print("Status: ONLINE (200 OK)")
    except urllib.error.URLError as e:
        print(f"Status: OFFLINE. Error: {e.reason}")

if __name__ == "__main__":
    check_health()
