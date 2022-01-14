import requests as r

print(r.__version__)
res = r.get('http://www.google.com/')
print(res.text)
res2 = r.get('http://raw.githubusercontent.com/Lildonk/cmput404lab/master/requestsVersion.py')
print(res2.text)