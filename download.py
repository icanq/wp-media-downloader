import xml.etree.ElementTree as ET
import requests
import os

def extract_image_urls(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    namespace = {'wp': 'http://wordpress.org/export/1.2/'}

    urls = []
    for item in root.findall('channel/item'):
        for enclosure in item.findall('wp:attachment_url', namespace):
            urls.append(enclosure.text)
    return urls

def download_images(urls, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    total_files = len(urls)
    downloaded_files = 0

    for url in urls:
        file_name = os.path.join(download_folder, url.split('/')[-1])
        if os.path.exists(file_name):
            print(f"Already downloaded: {file_name}")
            continue

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            downloaded_files += 1
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {url}")

    if downloaded_files == 0:
        print("All files are already downloaded.")
    else:
        print(f"Finished downloading {downloaded_files} new files out of {total_files}.")

xml_file = 'mint.WordPress.2024-04-30.xml'
image_urls = extract_image_urls(xml_file)
print(f"Found {len(image_urls)} images.")

download_folder = 'downloaded_images'
download_images(image_urls, download_folder)
