import requests


url = "https://raw.githubusercontent.com/SpaceChuck/spkg-repo/main/snakeos-update/snake-update.py"
r = requests.get(url, allow_redirects=True)

open('exec/snakeos-update.py', 'wb').write(r.content)
