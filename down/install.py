import requests


url = "https://raw.githubusercontent.com/SpaceChuck/spkg-repo/main/down/down.py"
r = requests.get(url, allow_redirects=True)

open('exec/down.py', 'wb').write(r.content)
