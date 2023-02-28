import threading
import requests

# Set up your authorization header
headers = {
    "Authorization": "Basic xxxxxxxxxxxxxxxxx"
}

# Set up your cookies (if any)
cookies = {
    "cookie_name": "xxxxxxxxx"
}

# Open the wordlist file and read each line as a URL to check
with open("/mnt/xxx/Users/xxx/Desktop/1.txt") as f:
    url_list = f.readlines()

# Define a function to check the response for a single URL
def check_url(url):
    url = url.strip()  # Remove any whitespace or newline characters
    try:
        response = requests.get(url, headers=headers, cookies=cookies)

        # Check the status code of the response
        if response.status_code == 200:
            print(f"{url} is accessible.")
        else:
            print(f"{url} returned a {response.status_code} status code.")
    except requests.exceptions.RequestException as e:
        print(f"{url} could not be accessed: {e}")

# Define the number of threads to use
num_threads = 50

# Create a list to hold the thread objects
threads = []

# Create the threads and start them
for i in range(num_threads):
    thread = threading.Thread(target=lambda: [check_url(url) for url in url_list[i::num_threads]])
    thread.start()
    threads.append(thread)

# Wait for all the threads to finish
for thread in threads:
    thread.join()
