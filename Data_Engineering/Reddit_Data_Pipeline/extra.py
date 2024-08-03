import socket
import requests

def test_dns_resolution():
    try:
        print("Resolving www.reddit.com...")
        ip = socket.gethostbyname('www.reddit.com')
        print(f"www.reddit.com resolved to {ip}")
    except socket.gaierror as e:
        print(f"DNS resolution error: {e}")

def test_http_connection():
    try:
        print("Connecting to https://www.reddit.com...")
        response = requests.get('https://www.reddit.com')
        print(f"HTTP response status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP connection error: {e}")

if __name__ == "__main__":
    test_dns_resolution()
    test_http_connection()
