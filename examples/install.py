import requests


url = "https://raw.githubusercontent.com/SpaceChuck/SnakeOS/main/exec/examples.py"
r = requests.get(url, allow_redirects=True)

open('exec/examples.py', 'wb').write(r.content)
