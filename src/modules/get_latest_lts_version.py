from bs4 import BeautifulSoup
import urllib.request, urllib.error

def get_latest_lts_version():
    try:
        # Request and read HTML content from the Node.js page
        with urllib.request.urlopen("https://nodejs.org/en/") as response:
            full_html = response.read().decode("utf-8")

        # Parse HTML and find the <b> element containing the version
        soup = BeautifulSoup(full_html, "html.parser")
        node = soup.find("b")

        return node.text if node else None
    except urllib.error.URLError as e:
        print(f"URL error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

latest_lts_version = get_latest_lts_version()
