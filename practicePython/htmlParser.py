from html.parser import HTMLParser

# create a subclass and override the handler methods

class MyHTMLParser(HTMLParser):
    flag=False
    def handle_starttag(self, tag, attrs):
        pass
        if tag == "h1":
          MyHTMLParser.flag=True
        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if MyHTMLParser.flag:
          print("Encountered some data  :", data)
          MyHTMLParser.flag=False

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1>'
            '<h2>Hello World</h1>'
            '<h1>Hai world</h1></body></html>')
