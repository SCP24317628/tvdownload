import requests
from bs4 import BeautifulSoup
import zipfile
import shutil
import os
import tempfile

def get_edgedriver_version():
    url = 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        version_code = None
        for link in soup.find_all('a'):
            if 'Latest stable release' in link.text:
                version_code = link.text.split()[-1]
                break
        if not version_code:
            raise Exception("Could not find EdgeDriver version.")
        return version_code
    else:
        raise Exception(f"Failed to retrieve version, status code: {response.status_code}")

def download_edgedriver(download_link, download_path):
    response = requests.get(download_link)
    if response.status_code == 200:
        with open(download_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download EdgeDriver, status code: {response.status_code}")

def unzip_edgedriver(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def main():
    try:
        edgedriver_version = get_edgedriver_version()
        download_link = f"https://msedgedriver.azureedge.net/{edgedriver_version}/edgedriver_win64.zip"

        with tempfile.TemporaryDirectory() as tmpdirname:
            zip_path = os.path.join(tmpdirname, 'edgedriver.zip')
            extract_path = os.path.join(tmpdirname, 'edgedriver')

            download_edgedriver(download_link, zip_path)
            unzip_edgedriver(zip_path, extract_path)

            file_source = os.path.join(extract_path, 'msedgedriver.exe')
            file_destination = './msedgedriver.exe'

            shutil.move(file_source, file_destination)
            print(f"EdgeDriver moved to {file_destination}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
