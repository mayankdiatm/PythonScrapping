from bs4 import BeautifulSoup
import requests
res = requests.get('http://spvss-gpk-bot01.cisco.com:10082/tags/STB_SW.git?branch=master')
type(res)
res.status_code
print(res.text[:1000])

