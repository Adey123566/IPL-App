import requests
import time

def test_server():
    print("Testing server connection...")
    try:
        response = requests.get('http://127.0.0.1:5000')
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text[:100]}...")  # Print first 100 chars
        return True
    except requests.exceptions.ConnectionError:
        print("Could not connect to server")
        return False

if __name__ == "__main__":
    # Wait a bit for the server to start
    print("Waiting for server to start...")
    time.sleep(2)
    test_server() 