import zipfile
import requests
from tqdm import tqdm
import os

def download(url,filename):
    r = requests.get(url, allow_redirects=True)
    total_size_in_bytes= int(r.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    # open(filename, 'wb').write(r.content)
    with open(filename, 'wb') as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

print("Downloading SnakeOS...")
download("https://github.com/SpaceChuck/SnakeOS/blob/main/Latest%20version%20of%20SnakeOS.zip?raw=true", "snakeos.zip")
print("Downloaded SnakeOS!")
i = input("Do you want to update SnakeOS? THIS WILL OVERWRITE YOUR CURRENT INSTALLATION! (Y/N):")
if i.lower() == "y":
    with zipfile.ZipFile("snakeos.zip", 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())
    os.remove("snakeos.zip")
    print("Now type 'python main.py'")
    exit()
