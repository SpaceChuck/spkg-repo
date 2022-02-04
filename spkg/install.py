import requests


url = "https://raw.githubusercontent.com/SpaceChuck/spkg-repo/main/spkg.py"
r = requests.get(url, allow_redirects=True)

open('exec/spkg.py', 'wb').write(r.content)
