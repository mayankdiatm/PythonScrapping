from suds.client import Client

url="http://www.webservicex.net/stockquote.asmx?WSDL"
client = Client(url)
print(client) ## shows the details of this service
res = client.service.GetQuote()

print(res)