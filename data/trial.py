import requests
from bs4 import BeautifulSoup

# Base URL for the Python documentation
base_url = "https://docs.python.org/3/tutorial/introduction.html"

# Get the HTML content of the webpage
response = requests.get(base_url)

# Check for successful response
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links within the page
    links = soup.find_all("a")

    # Extract and print the href (link) attribute from each link
    for link in links:
        if link.has_attr("href") and link["href"].endswith(".html"):
            # Extract the relative file path
            file_path = link["href"]
            # Print the full URL of the linked file
            print(f"{base_url}{file_path}")
else:
    print("Failed to download the webpage content.")
