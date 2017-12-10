#Example for parsing and processing HTML

import urllib.request
import urllib.error
from html.parser import HTMLParser

#create sub class and override the handler methods
class GoogleHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print ("Encounted comment: " + str(data))
    def handle_starttag(self,tag,attrs):
        pos = self.getpos()
        print ("Encounted start tag: " + str(tag) + " " + str(attrs) + " at line: " + str(pos[0]) + " position: " + str(pos[1]))
        if len(attrs):
            for a in attrs:
                if (a[0] and a[1]):
                    print(str(a[0]) + "=" + str(a[1]))


def main():
    try:
        googleUrl = urllib.request.urlopen("http://www.google.com")
    except urllib.error.URLError as e:
        print ("Error opening URL " + e.reason + str(e.errno))
        return

    if (googleUrl.getcode() == 200):
        data = googleUrl.read()
        print (data)

        data = data[2:]
        parser = GoogleHTMLParser()
        parser.feed(str(data))
    else:
        print ("Error urlopen code is " + str(googleUrl.getcode()))


if __name__ == "__main__":
    main()