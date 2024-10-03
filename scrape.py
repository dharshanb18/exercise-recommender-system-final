from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os
import urllib.parse

# Function to download images based on a search query
def download_images(query):
    # Encode the query for URL
    query_encoded = urllib.parse.quote(query)
    url = f'https://www.google.com/search?hl=en&tbm=isch&q={query_encoded}'

    os.makedirs('downloaded_images', exist_ok=True)

    try:
        htmldata = urlopen(url)
        soup = BeautifulSoup(htmldata, 'html.parser')
        images = soup.find_all('img')

        # Limit to top 10 images
        for index, item in enumerate(images[:5]): #top 5 images
            img_url = item.get('src')

            # Handle relative URLs
            if img_url and img_url.startswith('/'):
                img_url = url + img_url

            if img_url:  # Check if the URL is valid
                try:
                    # Create a filename based on the index
                    filename = os.path.join('downloaded_images', f'image_{index + 1}.jpg')
                    urlretrieve(img_url, filename)
                    print(f'Downloaded {filename}')
                except Exception as e:
                    print(f'Failed to download {img_url} - {e}')
    except Exception as e:
        print(f'Failed to open URL {url} - {e}')

query=input("enter the query")
download_images(query)
