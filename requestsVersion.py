import requests as r

print(r.__version__)
res = r.get('http://www.google.com/')
print(res.text)