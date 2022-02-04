import os
import requests
from tqdm import tqdm

argsfile = open(os.path.join("exec", "args.txt"), "r")
argsTemp = argsfile.readlines()
args = []
for i in argsTemp:
    if i == argsTemp[len(argsTemp)-1]:
        args.append(i)
    else:
        args.append(i[0:-1])
infofile = open(os.path.join("exec", "info.txt"), "r")
infoTemp = infofile.readlines()
info = []
for i in infoTemp:
    if i == infoTemp[len(infoTemp)-1]:
        info.append(i)
    else:
        info.append(i[0:-1])
def download(url,filename):
    r = requests.get(url, allow_redirects=True)
    total_size_in_bytes= int(r.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

username = info[0]
dir = info[1]
try:
    url = args[0]

except IndexError:
    print("""
    down - download files from the internet

    usage:
    down <url> <file>
    """)
    raise KeyboardInterrupt
try:
    filename = args[1]
except IndexError:
    print("""
    down - download files from the internet

    usage:
    down <url> <file>
    
    missing argument <file>
    """) 
    raise KeyboardInterrupt
download(url,os.path.join(dir,filename))
