import urllib.request

res = urllib.request.urlopen('http://www.google.co.in')
print(  res.read() )
