from bs4 import BeautifulSoup
import requests
res = requests.get('')
type(res)
res.status_code
print(res.text[:1000])

