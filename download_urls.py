import requests
from time import sleep

def download_content(urls, retries=3):
    for url in urls:
        for attempt in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                print(f"Downloaded content from {url}")
                break
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                if attempt < retries - 1:
                    sleep(2 ** attempt)  # Exponential backoff
                else:
                    print(f"Failed to download {url} after {retries} attempts")

# Example usage:
urls = ['http://example.com', 'http://nonexistenturl.com']
download_content(urls)
