import sys
import requests

def main():
    # Check if a URL was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
        return

    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            print(f"The website at '{url}' is reachable.")
        else:
            print(f"The website at '{url}' returned a status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()