import requests


url = "https://raw.githubusercontent.com/SpaceChuck/SnakeOS/main/exec/calc.py"
r = requests.get(url, allow_redirects=True)

open('exec/calc.py', 'wb').write(r.content)

