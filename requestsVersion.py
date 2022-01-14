import requests as r

print(r.__version__)
res = r.get('http://www.google.com/')
print(res.text)
res2 = r.get('http://github.com/Lildonk/cmput404lab.git')
print(res2.text)