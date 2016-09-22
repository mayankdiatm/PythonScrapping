from bs4 import BeautifulSoup
import requests
import re

url = "http://spvss-gpk-bot01.cisco.com:10082/tags/STB_SW.git?branch=master"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
links = soup.find_all("a")
if len(links) > 0:
    firstLink = links[0]
    errorMessage = []
    firstLink = str(firstLink)
    try:
        expectedVersion = re.match(r'.*>.*\/(.*)<.*', firstLink, re.M | re.I).group(1)
        print expectedVersion
        #expectedVersion = "D91.0.9"
        version = expectedVersion.split('D')[1]
        versionObject =  re.match(r'(\d*)\.(\d*)\.(\d*)', version, re.M | re.I)
        v1 = int(versionObject.group(1))
        v2 = int(versionObject.group(2))
        v3 = int(versionObject.group(3))
        print str(versionObject.group(1)) + "  - " + str(versionObject.group(2)) + "  - " + str(versionObject.group(3))

        if v3 < 9:
            v3 += 1
        elif v3 == 9:
            v3 = 0
            if v2 < 9:
                v2 += 1
            else:
                v2 = 0
                v1 += 1
        nextVersion =  "D" + str(v1) + "." + str(v2) + "." + str(v3)
        print "Next Version = " + nextVersion



    except Exception:
        errorMessage.append(firstLink + "\n")
print errorMessage








