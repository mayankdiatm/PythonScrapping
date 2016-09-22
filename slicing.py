

sample_url='http://coreyms.com'
print sample_url

#reverse the url
print sample_url[::-1]

#Get the top level domain
print sample_url[-4:]

# Print url without the http://
print sample_url[7:]


# Print url without the http:// or top level domain
print sample_url[7:-4]
